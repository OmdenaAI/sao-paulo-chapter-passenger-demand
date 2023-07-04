#######################
####### IMPORTS #######
#######################

# import required libraries
import os
import pickle
from   pathlib                       import Path
import numpy                         as     np
import pandas                        as     pd
import seaborn                       as     sns
import matplotlib.pyplot             as     plt
import matplotlib.patches            as     mpatches
import streamlit                     as     st
import statsmodels.formula.api       as     smf
from   statsmodels.tsa.arima.model   import ARIMA

# set fivethirtyeight style
plt.style.use("fivethirtyeight")


#########################
####### FUNCTIONS #######
#########################

def load_artifacts(line):
    """
    Load all required binaries for the given train line.

    Args
        line: an integer with the train line number
    
    Return
        tuple with artifacts loaded
    """

    # open file with context manager
    with open(os.path.join("artifacts", "production_models_summary"), "rb") as file:
        # load data
        all_performs = pickle.load(
            file
            )

    # open file with context manager
    with open(os.path.join("artifacts", f"sarima_line_{line}_model"), "rb") as file:
        # load model
        prod_arima = pickle.load(
            file, 
            )

    # open file with context manager
    with open(os.path.join("artifacts", "prediction_dataframe"), "rb") as file:
        # load model
        df_perform_pos_covid = pickle.load(
            file, 
            )

    # open file with context manager
    with open(os.path.join("artifacts", "causal_dataframe"), "rb") as file:
        # load model
        df_causal = pickle.load(
            file, 
            )

    return (df_perform_pos_covid, prod_arima, all_performs, df_causal)



#########################
####### STREAMLIT #######
#########################

# define page config

st.set_page_config(
    page_title='Modelling - Omdena São Paulo Brazil Chapter',
    layout='wide',
    initial_sidebar_state='collapsed',
    page_icon='images/omdena_logo.png',
    menu_items={'Get Help': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'Report a bug': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'About': '###### Developed by Omdena São Paulo, Brazil Local Chapter'}
)

# define title
st.title("Predictions and Causal Inference")
st.markdown("---")

# create two columns
_, mid_col, _l = st.columns(spec=[0.1, 0.8, 0.1], gap="small")

# open middel column
with mid_col:
    # let the user choose train line
    st.subheader("Choose train line:")
    line = st.radio(
        label="",  
        options=[1, 2, 3, 4, 5],#, 15], 
        index=0, 
        horizontal=True, 
        label_visibility="visible"
        )
# create a break
st.markdown("---")

# create two columns for plots
col_pred_plot, col_causal_plot = st.columns(spec=2, gap="large")
col_pred_text, col_causal_text = st.columns(spec=2, gap="large")

# load required artifacts
df_perform_pos_covid, prod_arima, all_performs, df_causal = load_artifacts(line)
# define required variables
target_variable, lead_time, forecast_horizon = 'total_millions', 1, 3        



###########################
####### PREDICTIONS #######
###########################

# open prediction column
with col_pred_plot:
    # define column head
    st.subheader("Predictions")

    # filter required line
    df_perform_pos_covid_line = df_perform_pos_covid.loc[
            df_perform_pos_covid["line"]==line, 
            [target_variable, "date"]
            ]
    # make predictions with production model
    forecast = prod_arima.get_forecast(
        steps=(lead_time+forecast_horizon)
        )
    # merge prediction and confidence intervals
    df_predictions = pd.merge(left=forecast.predicted_mean.to_frame(), 
            right=forecast.conf_int(),
            how="inner", left_index=True, right_index=True
            ).reset_index(names=["date"])

    # create columns with labels
    df_perform_pos_covid_line["origin"] = "real"
    df_predictions["origin"] = "prediction"
    # rename columns to concatenate
    df_predictions = df_predictions.rename(columns={"predicted_mean": "total_millions"})
    # concatenate dataframe
    df_plot = pd.concat(objs=[df_perform_pos_covid_line, df_predictions], axis=0)
    # get ci data
    df_plot_ci = df_plot[df_plot["origin"] == "prediction"]

    # sanity check
    assert (
        df_plot.shape[1] == df_predictions.shape[1]
        ) & (
        df_plot.shape[0] == df_perform_pos_covid_line.shape[0] + df_predictions.shape[0]
        ), "Missing rows and/or columns on concatenation"

    # get latest available point
    df_gap_ci = df_plot[df_plot["origin"]=="real"].tail(1)
    df_gap_ci["upper total_millions"] = df_gap_ci[target_variable]
    df_gap_ci["lower total_millions"] = df_gap_ci[target_variable]

    # get shape before concatenation
    shape_before = df_plot_ci.shape

    # concatenate df_gap to df_plot_ci 
    # so no space gap on plot between real and predictions
    df_plot_ci = pd.concat(objs=[df_plot_ci, df_gap_ci], axis=0)
    # sort by data
    df_plot_ci = df_plot_ci.sort_values(by=["date"])

    # sanity check
    assert (
        df_plot_ci.shape[0] == shape_before[0] + 1
        ) & (
        shape_before[1] == df_plot_ci.shape[1] == df_gap_ci.shape[1]
        ), "Missing rows and/or columns on concatenation"

    # get latest real value and first prediction
    df_plot_main = pd.concat(objs=[
        df_plot[df_plot["origin"] == "real"].tail(1),
        df_plot[df_plot["origin"] == "prediction"].head(1)
        ], axis=0)

    # instanciate object
    fig, ax = plt.subplots()
    # plot
    sns.lineplot(data=df_plot, x="date", y="total_millions", hue="origin",
                 palette={"real": "#FC4F30", "prediction":"#008FD5"}, ax=ax)
    sns.lineplot(data=df_plot_main, x="date", y="total_millions", 
                 color="#008FD5", ax=ax, linestyle="-")
    ax.fill_between(
        x=df_plot_ci["date"],
        y1=df_plot_ci["upper total_millions"],
        y2=df_plot_ci["lower total_millions"],
        color="#E5AE38",
        alpha=0.5,
        linestyle=":",
        linewidth=2, 
    )
    # define plot details
    ax.set_title(f"Passengers transported for line {line}")
    ax.set_ylabel("Number of passengers transported \n(in millions)")
    ax.set_xlabel("Date")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.legend(handles=[
        mpatches.Patch(color='#FC4F30', label='Observed'),
        mpatches.Patch(color='#008FD5', label='Predicted'),
        mpatches.Patch(color='#E5AE38', label='Confidence interval'),
        ],
        loc="upper left")
    # display on streamlit
    st.pyplot(fig=fig, use_container_width=True)

# open prediction column
with col_pred_text:
    # write add info
    st.markdown(f"""
Chosen model: **{all_performs[line]["model"].upper()}**

Model params: **{all_performs[line]["training_params"]["order"]}{all_performs[line]["training_params"]["seasonal_order"]}**

Validation method:
- **time-series cross-validation** with {all_performs[line]["ts_cv_n_splits"]} folds, test size of {all_performs[line]["ts_cv_test_size"]} months and gap of {all_performs[line]["ts_cv_gap"]} month

Performance metrics:
- **MAPE = {all_performs[line]["perform_summary"]["mape"]}**
- MPE = {all_performs[line]["perform_summary"]["mpe"]}
- MAE = {all_performs[line]["perform_summary"]["mae"]}
- RMSE = {all_performs[line]["perform_summary"]["rmse"]}
- RMSLE = {all_performs[line]["perform_summary"]["rmsle"]}
""")   



################################
####### CAUSAL INFERENCE #######
################################

# open causal column
with col_causal_plot:
    # define column head
    st.subheader("Causal inference")



    ########################################
    ####### REGRESSION DISCONTINUITY #######
    ########################################

    # filter required cokumns
    df_rd_line = df_causal.loc[
        df_causal["line"] == line,
        ["date", "total", "line"]
        ]
    # create a colum for total in millions
    df_rd_line[target_variable] = df_rd_line["total"].copy() / 1_000_000
    # create a new column with datetime index
    df_rd_line["year_month_idx"] = np.arange(start=0, stop=len(df_rd_line), step=1)

    # define discontinuity point
    d_point = 39
    # create a new column where discontinuity is on index 0
    df_rd_line["discontinuity_idx"] = df_rd_line["year_month_idx"] - d_point
    # create a new column to indicate if after discountinuity
    df_rd_line["treatment"] = df_rd_line["discontinuity_idx"] >= 0

    # use OLS to infer causality by means of coefficients
    model = smf.wls(f"{target_variable} ~ discontinuity_idx * treatment", df_rd_line).fit()

    # create a new column with predictions and errors
    df_rd_line["predictions"] = model.predict()
    df_rd_line["residuals"] = model.resid

    # create a copy of dataframe
    df_rd_line_counterfactual = df_rd_line[["discontinuity_idx", "treatment", "date"]].copy()
    # filter where where there were treatment
    df_rd_line_counterfactual = df_rd_line_counterfactual[df_rd_line_counterfactual["treatment"]]
    # assign treatment to zero 
    df_rd_line_counterfactual["treatment"] = False
    # make predictions
    df_rd_line_counterfactual["counterfactual_predictions"] = model.get_prediction(exog=df_rd_line_counterfactual).predicted_mean
    df_rd_line_counterfactual[
        ["counterfactual_predictions_lower_ci", "counterfactual_predictions_upper_ci"]
        ] = model.get_prediction(exog=df_rd_line_counterfactual).conf_int()

    # instanciate object
    fig = plt.figure()
    # plot original data as well as predictions
    ax = sns.scatterplot(data=df_rd_line, 
                         x="date", y=target_variable, 
                         color="#FC4F30", label="real")
    sns.lineplot(data=df_rd_line[df_rd_line["discontinuity_idx"]<0], 
                x="date", y="predictions", color="#008FD5", ax=ax, label="predicted", 
                linestyle="-", linewidth=2)
    sns.lineplot(data=df_rd_line[df_rd_line["discontinuity_idx"]>=0], 
                x="date", y="predictions", color="#008FD5", ax=ax, #label="predicted",
                linestyle="-", linewidth=2)
    sns.lineplot(data=df_rd_line_counterfactual.head(4), 
                x="date", y="counterfactual_predictions", color="#4F7032", ax=ax, label="counterfactual",
                linestyle=":", linewidth=2)
    ax.fill_between(
        x=df_rd_line_counterfactual["date"].head(4), 
        y1=df_rd_line_counterfactual["counterfactual_predictions_lower_ci"].head(4), 
        y2=df_rd_line_counterfactual["counterfactual_predictions_upper_ci"].head(4), 
        color="#E5AE38", linestyle=":", linewidth=2, alpha=0.5
        )
    # plot details
    ax.axvline(pd.to_datetime("2020-03", format="%Y-%m"), color="#4F7032", linestyle="--", linewidth=2)
    ax.set_title(f"Regression discontinuity for line {line}")
    ax.set_ylabel("Number of passengers transported \n(in millions)")
    ax.set_xlabel("Date")
    ax.legend(handles=[
        mpatches.Patch(color='#FC4F30', label='Observed'),
        mpatches.Patch(color='#008FD5', label='Predicted'),
        mpatches.Patch(color='#E5AE38', label='Counterfactual'),
        ],
        loc="lower left"
    )
    # display on streamlit
    st.pyplot(fig=fig, use_container_width=True)

# open causal column
with col_causal_text:

    # check for statistical significance
    if model.pvalues["treatment[T.True]"] < 0.05:
        # display report
        st.markdown(f"""       
According to **Regression Discontinuity** technique, the number of people transported on line {line} **reduced** by **{np.abs(model.params["treatment[T.True]"]):.3f} millions** due to **Covid** beginning.\n
""")