from dash import Dash, dcc, html, dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from dash import dash_table
from sqlalchemy import create_engine
import streamlit as st
from streamlit_option_menu import option_menu




mydb={
    "host":"localhost",
    "user":'root',
    "password":"",
    "database": "phonepe"
}
engine = create_engine('mysql+mysqlconnector://{user}:{password}@{host}/{database}'.format(**mydb))
cont="SELECT * FROM top_user_tab"
df1 = pd.read_sql_query(cont,engine)
df2 =pd.read_sql_query("select *from top_trans_tab",engine)
df3 =pd.read_sql_query("select *from arg_trans_tab",engine)
df4 =pd.read_sql_query("select *from map_trans_tab",engine)
df5 =pd.read_sql_query("select *from map_user_tab",engine)
df6 =pd.read_sql_query("select *from arg_user_tab",engine)


mapping={"andaman-&-nicobar-islands":"Andaman & Nicobar","andhra-pradesh":"Andhra Pradesh",'arunachal-pradesh':"Arunachal Pradesh",'assam':"Assam",'bihar':"Bihar",'chhattisgarh':"Chhattisgarh",'dadra-&-nagar-haveli-&-daman-&-diu':"Dadra and Nagar Haveli and Daman and Diu",'delhi':"Delhi",'goa':"Goa",'gujarat':"Gujarat",'haryana':"Haryana",'himachal-pradesh':"Himachal Pradesh",'jammu-&-kashmir':"Jammu & Kashmir",'jharkhand':"Jharkhand",'karnataka':"Karnataka",'kerala':"Kerala",'ladakh':"Ladakh",'lakshadweep':"Lakshadweep",'madhya-pradesh':"Madhya Pradesh",'maharashtra':"Maharashtra",'manipur':"Manipur",'meghalaya':"Meghalaya",'mizoram':"Mizoram",'nagaland':"Nagaland",'odisha':"Odisha",'puducherry':"Puducherry",'punjab':"Punjab",'rajasthan':"Rajasthan",'sikkim':"Sikkim",'tamil-nadu':"Tamil Nadu",'telangana':"Telangana",'tripura':"Tripura",'uttar-pradesh':"Uttar Pradesh",'uttarakhand':"Uttarakhand",'west-bengal':"West Bengal"}
df44=df2
df44["State"]=df44["State"].replace(mapping)







states = sorted(df1['State'].unique())
years = sorted(df1["Year"].unique())
Quarter = sorted(df2["Quarter"].unique())
Transaction_type=sorted(df3["Transaction_type"].unique())




st.markdown("PhonePe Pulse Data Analysis📶",style={'textAlign': 'center',"color":"purple","size":200})
    html.H5(children="Select the Quater⬇️"),
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in Quarter],
        value=Quarter[0], 
        clearable=False,
        style={"width":200}
    ),
    html.H5(children="Select the Year⬇️"),
    dcc.Dropdown(id='year-dropdown',
                 options=[{'label': year, 'value': year} for year in years],
                 value=years[0], 
                 clearable=False,
                 style={"width":200},
                 ),

    html.H2(children="Geo graph⬇️"),
    dcc.Graph(id="geo",style={"height":750}),


    html.H2(children="RegisteredUser⬇️"),
    dcc.Graph(
        id='life',style={"height":750}

    ),
    html.H2(children='Transaction Analysis💲💱',style={"color":"purple","textAlign":"center"}),
    html.H3(children="State Analysis:"),
    html.H5(children="Please select the state⬇️"),
     dcc.Dropdown(id='stateselection',
                 options=[{'label': state, 'value': state} for state in states],
                 value=states[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    html.H5(children="Please select the Transaction Type⬇️"),
    dcc.Dropdown(id='transactiontype_selection',
                 options=[{'label': type, 'value': type} for type in Transaction_type],
                 value=Transaction_type[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    html.H5(children="Please select the Quarter⬇️"),
    dcc.Dropdown(id='Quarterselection',
                 options=[{'label': Quarter, 'value': Quarter} for Quarter in Quarter],
                 value=Quarter[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    dcc.Graph(
        id="newgr",style={"height":750}

    ),
    
    html.H3(children="District Analysis:"),
    html.H5(children="Please select the state⬇️"),
     dcc.Dropdown(id='stateselectionfordistrict',
                 options=[{'label': state, 'value': state} for state in states],
                 value=states[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    
    html.H5(children="Please select the Quarter⬇️"),
    dcc.Dropdown(id='Quarterselectionfordistrict',
                 options=[{'label': Quarter, 'value': Quarter} for Quarter in Quarter],
                 value=Quarter[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    html.H5(children="Please select the Year⬇️"),
    dcc.Dropdown(id="Year_selectionfordistrict",
                 options=[{'label': years, 'value': years} for years in years],
                 value=years[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    dcc.Graph(
        id="districtanaly",style={"height":750}

    ),
    html.H3(children="Yearly Analysis:"),
    html.H5(children="Please select the Transaction Type⬇️"),
    dcc.Dropdown(id='Typeselectionfordistrict',
                 options=[{'label': Quarter, 'value': Quarter} for Quarter in Transaction_type],
                 value=Transaction_type[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    html.H5(children="Please select the Year⬇️"),
    dcc.Dropdown(id='Year_selectionfordistrict1',
                 options=[{'label': years, 'value': years} for years in years],
                 value=years[0], 
                 clearable=False,
                 style={"width":200},
                 ),
    dcc.Graph(
        id="districtanalyyear",
        style={"height":750}

    ),
    dcc.Graph(id="piecha"
              ),

    html.Div([
        html.H1(children="User Data Analysis", style={"textAlign":"center","color":"purple"}),
        html.H3(children="State Analysis⬇️"),
        html.H5(children="Please select the State:"),
         dcc.Dropdown(
            id='state-dropdownuser',
            options=[{'label': state, 'value': state} for state in states],
            value=states[0],  
            clearable=False,
            style={"width":200}
        ),
        dcc.Graph(
            id='userdis',
            style={"height":750}),


        html.H3(children="District Analysis of Users:"),
        html.H5(children="Please select the State⬇️"),
        dcc.Dropdown(
            id='selectedstateuser',
            options=[{'label': state, 'value': state} for state in states],
            value=states[0],  
            clearable=False,
            style={"width":200}
        ),
        html.H5(children="Please select the Year⬇️"),
        dcc.Dropdown(
            id='selectedyearuser',
            options=[{'label': years, 'value': years} for years in years],
            value=years[0],  
            clearable=False,
            style={"width":200}
        ),
        html.H5(children="Please select the Quarter⬇️"),
        dcc.Dropdown(
            id='selectedquarteruser',
            options=[{'label': Quarter, 'value': Quarter} for Quarter in Quarter],
            value=Quarter[0],  
            clearable=False,
            style={"width":200}
        ),
        dcc.Graph(id="userapp",
                  style={"height":750}
                  ),

        html.H3(children="Yearly Analysis of Users:"),
        html.H5(children="Please select the State⬇️"),
        dcc.Dropdown(
            id='selectedstateuser1',
            options=[{'label': state, 'value': state} for state in states],
            value=states[0],  
            clearable=False,
            style={"width":200}
        ),
        html.H5(children="Please select the Year⬇️"),
        dcc.Dropdown(
            id='selectedyearuser1',
            options=[{'label': years, 'value': years} for years in years],
            value=years[0],  
            clearable=False,
            style={"width":200}
        ),
        
        dcc.Graph(id="userapp1",
                  style={"height":450}
                  ),
        html.H3(children="Over All User Analysis")  ,       
        dcc.Graph(id="userapp2",
                  style={"height":450}
                  ),
        dcc.Graph(id="userapp3",
                  style={"height":450}
                  ),

        html.H1(children="Total Transaction",style={"textAlign":"center","color":"purple"}),
        html.H5(children="Please select the Quarter⬇️"),
        dcc.Dropdown(
            id='state-dropdown1',
            options=[{'label': state, 'value': state} for state in Quarter],
            value=Quarter[0],  
            clearable=False,
            style={"width":200}
        ),
        html.H5(children="Please Select the Year⬇️"),
        dcc.Dropdown(id='year-dropdown1',
                     options=[{'label': year, 'value': year} for year in years],
                     value=years[0], 
                     clearable=False,
                     style={"width":200},
                     

                     ),
        html.H3(children="Graph of Total Transaction"),
        dcc.Graph(
            id='life1',
            style={"height":750}

        ),
        
        html.H4(children="Top 3 Transaction amount by states"),
        dash_table.DataTable(
            id="tabletoptrans",
            columns=[{'name': col, 'id': col} for col in ["State", "Transaction_amount"]],
            page_size=3,
            

            
        ),
        html.H4(children="Top 3 Transaction count by states"),
        dash_table.DataTable(
            id="tabletoptranscount",
            columns=[{'name': col, 'id': col} for col in ["State", "Transaction_count"]],
            page_size=3,

            
        ),
           html.H4(children="Top 3 states with high registered users"),
           dash_table.DataTable(
            id="tabletopregisteruser",
            columns=[{'name': col, 'id': col} for col in ["State", "RegisteredUsers"]],
            page_size=3,
        )
    ]),
])
])


@app.callback(
    [Output(component_id='life', component_property='figure'),
     Output(component_id='newgr', component_property='figure'),
     Output(component_id='life1', component_property='figure'),
     Output(component_id="tabletoptrans", component_property="data"),
     Output(component_id="tabletoptranscount", component_property="data"),
     Output(component_id="tabletopregisteruser", component_property="data"),
     Output(component_id="districtanaly",component_property="figure"),
     Output(component_id="districtanalyyear",component_property="figure"),
     Output(component_id="piecha",component_property="figure"),
     Output(component_id="userdis",component_property="figure"),
     Output(component_id="userapp",component_property="figure"),
     Output(component_id="userapp1",component_property="figure"),
     Output(component_id="userapp2",component_property="figure"),
     Output(component_id="userapp3",component_property="figure"),
     Output(component_id="geo",component_property="figure"),
     ],

    [Input('state-dropdown', 'value'),
     Input("year-dropdown", "value"),
     Input('state-dropdown1', 'value'),
     Input("year-dropdown1", "value"),
     Input("stateselection","value"),
     Input("transactiontype_selection","value"),
     Input("Quarterselection", "value"),
     Input("stateselectionfordistrict","value"),
     Input("Quarterselectionfordistrict","value"),
     Input("Year_selectionfordistrict", "value"),
     Input("Typeselectionfordistrict","value"),
     Input("Year_selectionfordistrict1","value"),
     Input("state-dropdownuser","value"),
     Input("selectedstateuser","value"),
     Input("selectedyearuser","value"),
     Input("selectedquarteruser","value"),
     Input("selectedstateuser1","value"),
     Input("selectedyearuser1","value"),]
)

def update_graph(selected_state, selected_year, selected_state1, selected_year1,stateselection,Transactiontype_selection,Quarterselection,diststate,disquarter,disyear,Typeselectionfordistrict,Year_selectionfordistrict1,state_dropdownuser,selectedstateuser,selectedyearuser,selectedquarteruser,selectedstateuser1,selectedyearuser1):
    filtered_df = df1[(df1['Quarter'] == selected_state) & (df1["Year"] == selected_year)]
    filtered_df1 = df2[(df2['Quarter'] == selected_state1) & (df2["Year"] == selected_year1)]
    fortransaction=df3[(df3["State"]==stateselection) & (df3["Transaction_type"]==Transactiontype_selection) & (df3['Quarter'] == Quarterselection)]
    districtselection=df4[(df4["State"]==diststate) & (df4["Year"]==disyear) & (df4['Quarter'] == disquarter)]
    districtselection1 = df3[(df3["Transaction_type"] == Typeselectionfordistrict) & (df3["Year"] == Year_selectionfordistrict1)]
    userstate=df5[(df5["State"])==state_dropdownuser]
    userdistr = df5[(df5["State"] == selectedstateuser) & (df5["Year"] == selectedyearuser) & (df5["Quarter"] == selectedquarteruser)]
    userdistr1 = df6[(df6["State"] == selectedstateuser1) & (df6["Year"] == selectedyearuser1)]
    geoselect=df44[(df44["Year"]==selected_year) & (df44["Quarter"]==selected_state)]


    grouped_df = filtered_df1.groupby(['State', 'Year'])['Transaction_amount'].sum().reset_index()
    grouped_df1 = filtered_df1.groupby(['State', 'Year'])['Transaction_count'].sum().reset_index()
    grouped_df_registereduser = filtered_df.groupby(["State", "Year"])["RegisteredUsers"].sum().reset_index()
    grouped_df_Transaction= fortransaction.groupby(["State","Transaction_type","Quarter","Year","Transaction_amount"])["Transaction_count"].sum().reset_index()
    grouped_df_trans_year= districtselection1.groupby(["Year","Transaction_type","State"])[["Transaction_count","Transaction_amount"]].sum().reset_index()
    piee_df=df3.groupby(["Year"])["Transaction_count"].sum().reset_index()
    userdist=userstate.groupby(["State","Year"])[["RegisteredUser","AppOpens"]].sum().reset_index()
    userdisapp=userdistr.groupby(["State","Year","Quarter","District"])["AppOpens"].sum().reset_index()
    userdisapp1=userdistr1.groupby(["State","Year","Quarter","Brand"])["count"].sum().reset_index()
    useroverall=df5.groupby(["Year"])[["RegisteredUser","AppOpens"]].sum().reset_index()
    geogroup=geoselect.groupby(["Year","Quarter","State"])[["Transaction_count","Transaction_amount"]].sum().reset_index()
    
    
    sortit = grouped_df.sort_values(by="Transaction_amount", ascending=False)
    sortit1 = grouped_df1.sort_values(by="Transaction_count", ascending=False)
    sorted_register=grouped_df_registereduser.sort_values(by="RegisteredUsers",ascending=False)
    sorted_transc=grouped_df_Transaction.sort_values(by="Transaction_count",ascending=False)
    sorted_transc_year=grouped_df_trans_year.sort_values(by="Transaction_count",ascending=True)
      
    

    life = px.bar(sorted_register, x="State", y="RegisteredUsers", color="State", hover_data="RegisteredUsers",title="Graph of RegisteredUsers:")
    newgr = px.bar(sorted_transc, x="Year", y="Transaction_count",hover_data="Transaction_amount",title=f"State selected is {stateselection}")
    districtanaly = px.bar(districtselection, x="District", y="Count",labels={"Count":"Total_Transaction_Count","Amount":"Total_amount"},color="District",hover_data="Amount",title=f"State of {diststate} got {len(districtselection)} districts")
    districtanalyyear=px.bar(sorted_transc_year,x="State",y="Transaction_count",color="State",hover_data="Transaction_amount",title=f"Yearly Analysis of {Typeselectionfordistrict} in {Year_selectionfordistrict1} ")
    life1 = px.bar(sortit, x="State", y="Transaction_amount", color="State", hover_data="Transaction_amount",title="Transaction in States")
    piecha=px.pie(piee_df,values="Transaction_count",names="Year",hole=0.5,color_discrete_sequence=px.colors.sequential.Purp,title="Overall Transaction as Pie Chart")
    userdis=px.scatter(userdist,x="Year",y=["AppOpens","RegisteredUser"],title="Analysis of AppOpens and Registeredsers")
    userdis.update_traces(marker_size=20,marker_line_color="red",marker_symbol="circle")
    userapp=px.bar(userdisapp,x="District",y="AppOpens",title=f"State of {selectedstateuser} got {len(userdistr)} districts")
    userapp1=px.pie(userdisapp1,names="Brand",values="count",color_discrete_sequence=px.colors.sequential.Purp,title="User Analysis with Mobile Details",hole=0.5)
    userapp2=px.pie(useroverall,names="Year",values="AppOpens",title="Overall AppOpens Analysis")
    userapp3=px.pie(useroverall,names="Year",values="RegisteredUser",title="Overall Registered User Analysis")
    geo=px.choropleth(geogroup,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='State',
    hover_data=["Transaction_amount","Transaction_count"],
    color_continuous_scale='Reds')
    geo.update_geos(fitbounds="locations", visible=False)


    tabletoptrans = sortit[["State", "Transaction_amount"]].to_dict('records')
    tabletoptranscount = sortit1[["State", "Transaction_count"]].to_dict('records')
    tabletopregisteruser=sorted_register[["State","RegisteredUsers"]].to_dict("records")
    
    return life, newgr, life1, tabletoptrans,tabletoptranscount,tabletopregisteruser,districtanaly,districtanalyyear,piecha,userdis,userapp,userapp1,userapp2,userapp3,geo


if __name__ == '__main__':
    app.run_server(debug=True)


