import pandas as pd 
import folium
import os
from streamlit_folium import st_folium 
import streamlit as st 
import networkx as nx

pes_df = pd.read_csv(r"C:\OMDENA\Project\sao-paulo-chapter-passenger-demand\src\tasks\task_2_eda_dashboards\data\alllines_pes_complete.csv")
pes_df['date'] = pd.to_datetime(pes_df['date'])

metro_stations = {
    '1': [
        {'station': 'Jabaquara', 'coordinates': (-23.647253, -46.642808)},
        {'station': 'Conceição', 'coordinates': (-23.636450, -46.641791)},
        {'station': 'São Judas', 'coordinates': (-23.626218, -46.639498)},
        {'station': 'Saúde', 'coordinates': (-23.614919, -46.638143)},
        {'station': 'Praça da Árvore', 'coordinates': (-23.610576, -46.637861)},
        {'station': 'Santa Cruz', 'coordinates': (-23.599162 ,-46.636681)},
        {'station': 'Vila Mariana', 'coordinates': (-23.584878, -46.638107)},
        {'station': 'Ana Rosa', 'coordinates': (-23.581494, -46.638265)},
        {'station': 'Paraíso', 'coordinates': (-23.575, -46.640556)},
        {'station': 'Vergueiro', 'coordinates': (-23.568958, -46.63986)},
        {'station': 'São Joaquim', 'coordinates': (-23.563832, -46.640815)},
        {'station': 'Japão-Liberdade', 'coordinates': (-23.560361, -46.633196)},
        {'station': 'Sé', 'coordinates': (-23.550687, -46.633932)},
        {'station': 'São Bento', 'coordinates': (-23.543183, -46.631402)},
        {'station': 'Luz', 'coordinates': (-23.536579, -46.633468)},
        {'station': 'Tiradentes', 'coordinates': (-23.534333, -46.630981)},
        {'station': 'Armênia', 'coordinates': (-23.525122, -46.623554)},
        {'station': 'Portuguesa-Tietê', 'coordinates': (-23.516440, -46.623067)},
        {'station': 'Carandiru', 'coordinates': (-23.512454, -46.622729)},
        {'station': 'Santana', 'coordinates': (-23.505693, -46.624628)},
        {'station': 'Jardim São Paulo-Ayrton Senna', 'coordinates': (-23.503239, -46.609870)},
        {'station': 'Parada Inglesa', 'coordinates': (-23.496832, -46.606034)},
        {'station': 'Tucuruvi', 'coordinates': (-23.480844, -46.601547)},
    ],
    '2': [
        {'station': 'Vila Madalena', 'coordinates': (-23.548286, -46.694416)},
        {'station': 'Santuário N.S. de Fátima-Sumaré', 'coordinates': (-23.550637 ,-46.677588)},
        {'station': 'Clínicas', 'coordinates': (-23.5544, -46.6706)},
        {'station': 'Consolação', 'coordinates':  (-23.5575, -46.6608)},
        {'station': 'Trianon-Masp', 'coordinates': (-23.5625, -46.655)},
        {'station': 'Brigadeiro', 'coordinates': (-23.568811, -46.648098)},
        {'station': 'Paraíso', 'coordinates': (-23.575, -46.640556)},
        {'station': 'Ana Rosa', 'coordinates': (-23.581494, -46.638265)},
        {'station': 'Chácara Klabin', 'coordinates': (-23.592503, -46.629978)},
        {'station': 'Santos-Imigrantes', 'coordinates': (-23.595935 ,-46.620741)},
        {'station': 'Alto do Ipiranga', 'coordinates': (-23.602957, -46.611791)},
        {'station': 'Sacomã', 'coordinates': (-23.601519, -46.603446)},
        {'station': 'Tamanduateí', 'coordinates': (-23.5944, -46.5881)},
        {'station': 'Vila Prudente', 'coordinates': (-23.5845193 ,-46.5819991)},   
    ],
    '3': [
        {'station': 'Palmeiras-Barra Funda', 'coordinates': (-23.525505, -46.667358)},
        {'station': 'Marechal Deodoro', 'coordinates': (-23.5338615 ,-46.6558135)},
        {'station': 'Santa Cecília', 'coordinates': (-23.538711, -46.649644)},
        {'station': 'República', 'coordinates': (-23.544081,-46.642799)},
        {'station': 'Anhangabaú', 'coordinates': (-23.547917, -46.639345)},
        {'station': 'Sé', 'coordinates': (-23.550687, -46.633932)},
        {'station': 'Pedro II', 'coordinates': (-23.5500, -46.6258)},
        {'station': 'Brás', 'coordinates': (-23.547824, -46.615881)},
        {'station': 'Bresser-Moóca', 'coordinates': (-23.547824, -46.615881)},
        {'station': 'Belém', 'coordinates': (-23.5433, -46.5894)},
        {'station': 'Tatuapé', 'coordinates': (-23.540314, -46.576184)},
        {'station': 'Carrão', 'coordinates': (-23.5375, -46.5636)},
        {'station': 'Penha', 'coordinates': (-23.533439 ,-46.542302)},
        {'station': 'Vila Matilde', 'coordinates': (-23.531894 ,-46.530691)},
        {'station': 'Guilhermina-Esperança', 'coordinates': (-23.5292, -46.5167)},
        {'station': 'Patriarca', 'coordinates': (-23.531166 ,-46.501586)},
        {'station': 'Artur Alvim', 'coordinates': (-23.54055, -46.484265)},
        {'station': 'Corinthians-Itaquera', 'coordinates': (-23.542207, -46.471159)}
    ],
    '4': [
        {'station': 'Luz', 'coordinates': (-23.536579, -46.633468)},
        {'station': 'República', 'coordinates': (-23.544081, -46.642799)},
        {'station': 'Higienópolis - Mackenzie', 'coordinates': (-23.5488889, -46.6519444)},
        {'station': 'Paulista', 'coordinates': (-23.553164454, -46.657164038)},
        {'station': 'Oscar Freire', 'coordinates': (-23.5608583, -46.6720083)},
        {'station': 'Fradique Coutinho', 'coordinates': (-23.566169, -46.684267)},
        {'station': 'Faria Lima', 'coordinates': (-23.566667 ,-46.693889)},
        {'station': 'Pinheiros', 'coordinates': (-23.5667702 ,-46.7019)},
        {'station': 'Butantã', 'coordinates': (-23.571852, -46.708164)},
        {'station': 'São Paulo - Morumbi', 'coordinates': (-23.621667, -46.701667)},   
    ],
    '5': [
        {'station': 'Capão Redondo', 'coordinates': (-23.6592509, -46.7681766)},
        {'station': 'Campo Limpo', 'coordinates': (-23.6493743 ,-46.7591482)},
        {'station': 'Vila das Belezas', 'coordinates': (-23.640556, -46.745833)},
        {'station': 'Giovanni Gronchi', 'coordinates': (-23.643964, -46.7342466)},
        {'station': 'Santo Amaro', 'coordinates': (-23.655556, -46.720556)},
        {'station': 'Largo Treze', 'coordinates': (-23.654524 ,-46.710343)},
        {'station': 'Adolfo Pinheiro', 'coordinates': (-23.6501, -46.7042)},
        {'station': 'Alto da Boa Vista', 'coordinates': (-23.641944, -46.699722)},
        {'station': 'Borba Gato', 'coordinates': (-23.633333, -46.692778)},
        {'station': 'Brooklin', 'coordinates': (-23.627014, -46.688333)},
        {'station': 'Campo Belo', 'coordinates': (-23.618889, -46.682222)},
        {'station': 'Eucaliptos', 'coordinates': (-23.61, -46.668611)},
        {'station': 'Moema', 'coordinates': (-23.603611, -46.661944)},
        {'station': 'AACD - Servidor', 'coordinates': (-23.598308, -46.651600)},
        {'station': 'Hospital São Paulo', 'coordinates': (-23.598431, -46.645556)},
        {'station': 'Santa Cruz', 'coordinates': (-23.599162 ,-46.636681)},
        {'station': 'Chácara Klabin', 'coordinates': (-23.592503 ,-46.629978)},
        
    ],
    '15': [
        {'station': 'Jardim Colonial', 'coordinates': (-23.59921, -46.46907)},
        {'station': 'São Mateus', 'coordinates': (-23.61232, -46.4773)},
        {'station': 'Fazenda da Juta', 'coordinates': (-23.61182, -46.48747)},
        {'station': 'Sapopemba', 'coordinates': (-23.61471, -46.50083)},
        {'station': 'Jardim Planalto', 'coordinates': (-23.60616, -46.50785)},
        {'station': 'Vila União', 'coordinates': (-23.60297, -46.51556)},
        {'station': 'Vila Tolstói', 'coordinates': (-23.60084, -46.52722)},
        {'station': 'Camilo Haddad', 'coordinates': (-23.59544, -46.53759)},
        {'station': 'São Lucas', 'coordinates': (-23.58894, -46.54464)},
        {'station': 'Oratório', 'coordinates': (-23.58216, -46.5618)},
        {'station': 'Vila Prudente', 'coordinates': (-23.58443, -46.58194)},

    ]
}

month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

line_colors = {
    '1': 'blue',
    '2': 'green',
    '3': 'red',
    '4': 'yellow',
    '5': 'purple',
    '15': 'gray'
}


def ShowMap(month,year,line):
    # Create a map centered around São Paulo
    
    if line =='all':
        if (year==2023) and (month_mapping[month]>=5):
            st.markdown('Please Enter Month before May for the year 2023')
        
        
        else:
            map_sp = folium.Map(location=[-23.550520, -46.633308], zoom_start=12)



            # Iterate over each metro line
            for line, stations in metro_stations.items():
                # Get the color for the current line
                color = line_colors[line]

                # Iterate over each station
                for i in range(len(stations) - 1):
                    # Get the coordinates of the current station and the next station
                    current_station = stations[i]
                    next_station = stations[i + 1]
                    

                    # Add the station name as a marker
                    
                    filtered_df = pes_df[(pes_df['station'].str.strip()==current_station['station'])&(pes_df['date'].dt.year==year)&(pes_df['date'].dt.month==month_mapping[month])]
                    dpea_value = filtered_df['dpea']
                    
                    folium.CircleMarker(
                        location=current_station['coordinates'],
                        radius= (dpea_value.values[0]/3500),
                        color = color,
                        fill = True,
                        fill_color = color,
                        tooltip=f"Station: {current_station['station']}<br>Passengers: {dpea_value.values[0]}"
                        # popup=current_station['station'],
                        # icon=folium.Icon(color=color)
                    ).add_to(map_sp)
                    
                    # Create a line connecting the current station and the next station
                    folium.PolyLine(
                        locations=[current_station['coordinates'], next_station['coordinates']],
                        color=color,
                        weight=3,
                        opacity=0.7
                    ).add_to(map_sp)
                    
                folium.CircleMarker(
                    location=next_station['coordinates'],
                    radius= (dpea_value.values[0]/3500),
                    color = color,
                    fill = True,
                    fill_color = color,
                    tooltip=f"Station: {next_station['station']}<br>Passengers: {dpea_value.values[0]}"
                    # popup=current_station['station'],
                    # icon=folium.Icon(color=color)
                ).add_to(map_sp)
            st_map = st_folium(map_sp,width =1000,height = 700)
    else :
        
        if (year==2023) and (month_mapping[month]>=5):
            
            st.markdown('Please Enter Month before May for the year 2023')
        
        
        else:
            map_sp = folium.Map(location=[-23.550520, -46.633308], zoom_start=12)

            # Define colors for each metro line
            color = line_colors[line]

            for i in range(len(metro_stations.get(line))-1):
                    # Get the coordinates of the current station and the next station
                current_station = metro_stations.get(line)[i]
                next_station = metro_stations.get(line)[i + 1]
                    
                filtered_df = pes_df[(pes_df['station'].str.strip()==current_station['station'])&(pes_df['date'].dt.year==2021)&(pes_df['date'].dt.month==1)]
                dpea_value = filtered_df['dpea']
                    
                folium.CircleMarker(
                        location=current_station['coordinates'],
                        radius= (dpea_value.values[0]/3500),
                        color = color,
                        fill = True,
                        fill_color = color,
                        tooltip=f"Station: {current_station['station']}<br>Passengers: {dpea_value.values[0]}"
                        # popup=current_station['station'],
                        # icon=folium.Icon(color=color)
                    ).add_to(map_sp)
                    
                    # Create a line connecting the current station and the next station
                folium.PolyLine(
                        locations=[current_station['coordinates'], next_station['coordinates']],
                        color=color,
                        weight=3,
                        opacity=0.7
                    ).add_to(map_sp)
            folium.CircleMarker(
            location=next_station['coordinates'],
            radius= (dpea_value.values[0]/3500),
            color = color,
            fill = True,
            fill_color = color,
             tooltip=f"Station: {next_station['station']}<br>Passengers: {dpea_value.values[0]}"
            # popup=current_station['station'],
            # icon=folium.Icon(color=color)
                ).add_to(map_sp)
            st_map = st_folium(map_sp,width =1000,height = 700)
            


def CreateGraph():
    avg_time_df = pd.read_csv(r"C:\OMDENA\Project\sao-paulo-chapter-passenger-demand\src\tasks\task_3_model_training_validation\Ansh_models\metro_lines_info.csv")
    G = nx.Graph()
    # Add nodes for each metro station
    for line, stations in metro_stations.items():
        for station in stations:
            station_name = station['station']
            filtered_df = pes_df[(pes_df['station'].str.strip()==station_name)&(pes_df['date'].dt.year==2021)&(pes_df['date'].dt.month==1)]
            dpea_value = filtered_df['dpea']
            passengers = dpea_value.values[0]
            G.add_node(station_name, passengers=passengers,line = f"{line}")
    # Add edges between adjacent stations
    for line, stations in metro_stations.items():
        for i in range(len(stations) - 1):
            station1 = stations[i]['station']
            station2 = stations[i + 1]['station']
            time = avg_time_df[avg_time_df['Line']==int(line)]
            # print(time,"\n-------")
            avg_time = time['Avg Time between Stations (min)'].iloc[0]
            # print(avg_time,"\n-------")
            t = avg_time
            G.add_edge(station1, station2, weight = t)
    return G
# def TakeDestinations():
#     metro_sta = list(pes_df['station'].unique())
#     st.sidebar.header("Choose Stations")
#     start_station = st.sidebar.selectbox("Select start station", metro_sta)
#     end_station = st.sidebar.selectbox("Select end station", metro_sta)
#     FindShortest_path(start_station.strip(),end_station.strip())
    

def FindShortest_path(start_station,end_station):
    G = CreateGraph()
    # Check if the start and end stations are valid
    if start_station not in G.nodes() or end_station not in G.nodes():
        print("Invalid start or end station.")
    else:
        # Calculate the shortest path
        shortest_path = nx.dijkstra_path(G, start_station, end_station, weight='weight')
        print("Shortest Path:", shortest_path)

        # Create a map centered around São Paulo
        short_map = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        
        for i in range(len(shortest_path)-1):
            current_station = shortest_path[i]
            next_station = shortest_path[i+1]
            for line, stations in metro_stations.items():
                for station in stations:
                    if station['station'] == current_station:
                        coordinates_current = station['coordinates']
                        break
            for line, stations in metro_stations.items():
                for station in stations:
                    if station['station'] == next_station:
                        coordinates_next = station['coordinates']
                        break
        
                
            folium.CircleMarker(
                    location=coordinates_current,
                    radius= (G.nodes[current_station]['passengers'])/3500,
                    color = line_colors[G.nodes[current_station]['line']],
                    fill = True,
                    fill_color = line_colors[G.nodes[current_station]['line']],
                    tooltip=f"Station: {current_station}<br>Passengers: {G.nodes[current_station]['passengers']}"
                    # popup=current_station['station'],
                    # icon=folium.Icon(color=color)
                ).add_to(short_map)
                
                # Create a line connecting the current station and the next station
            folium.PolyLine(
                    locations=[coordinates_current,coordinates_next],
                    color=line_colors[G.nodes[current_station]['line']],
                    weight=3,
                    opacity=0.7
                ).add_to(short_map)
        folium.CircleMarker(
                        location=coordinates_next,
                        radius= (G.nodes[next_station]['passengers'])/3500,
                        color = line_colors[G.nodes[next_station]['line']],
                        fill = True,
                        fill_color = line_colors[G.nodes[current_station]['line']],
                        tooltip=f"Station: {next_station}<br>Passengers: {G.nodes[next_station]['passengers']}"
                        # popup=current_station['station'],
                        # icon=folium.Icon(color=color)
                    ).add_to(short_map)       
        st_map = st_folium(short_map,width =1000,height = 700)
        
def ShowEDA():
    pass
        

     
