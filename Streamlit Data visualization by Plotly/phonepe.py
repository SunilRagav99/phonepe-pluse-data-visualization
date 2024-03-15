import plotly.express as px
import pandas as pd
import json
import streamlit as st
from PIL import Image
from sqlalchemy import create_engine
from streamlit_option_menu import option_menu

# Database connection
mydb = {
    "host": "localhost",
    "user": 'root',
    "password": "",
    "database": "phonepe"
}
engine = create_engine('mysql+mysqlconnector://{user}:{password}@{host}/{database}'.format(**mydb))

# Data retrieval
cont = "SELECT * FROM top_user_tab"
df1 = pd.read_sql_query(cont, engine)
df2 = pd.read_sql_query("select * from top_trans_tab", engine)
df3 = pd.read_sql_query("select * from arg_trans_tab", engine)
df4 = pd.read_sql_query("select * from map_trans_tab", engine)
df5 = pd.read_sql_query("select * from map_user_tab", engine)
df6 = pd.read_sql_query("select * from arg_user_tab", engine)

mapping = {"andaman-&-nicobar-islands": "Andaman & Nicobar", "andhra-pradesh": "Andhra Pradesh",
           'arunachal-pradesh': "Arunachal Pradesh", 'assam': "Assam", 'bihar': "Bihar",
           'chhattisgarh': "Chhattisgarh", 'dadra-&-nagar-haveli-&-daman-&-diu': "Dadra and Nagar Haveli and Daman and Diu",
           'delhi': "Delhi", 'goa': "Goa", 'gujarat': "Gujarat", 'haryana': "Haryana",
           'himachal-pradesh': "Himachal Pradesh", 'jammu-&-kashmir': "Jammu & Kashmir", 'jharkhand': "Jharkhand",
           'karnataka': "Karnataka", 'kerala': "Kerala", 'ladakh': "Ladakh", 'lakshadweep': "Lakshadweep",
           'madhya-pradesh': "Madhya Pradesh", 'maharashtra': "Maharashtra", 'manipur': "Manipur",
           'meghalaya': "Meghalaya", 'mizoram': "Mizoram", 'nagaland': "Nagaland", 'odisha': "Odisha",
           'puducherry': "Puducherry", 'punjab': "Punjab", 'rajasthan': "Rajasthan", 'sikkim': "Sikkim",
           'tamil-nadu': "Tamil Nadu", 'telangana': "Telangana", 'tripura': "Tripura",
           'uttar-pradesh': "Uttar Pradesh", 'uttarakhand': "Uttarakhand", 'west-bengal': "West Bengal"}

df44 = df2
df44["State"] = df44["State"].replace(mapping)


states = sorted(df1['State'].unique())
years = sorted(df1["Year"].unique())
Quarter = sorted(df2["Quarter"].unique())
Transaction_type = sorted(df3["Transaction_type"].unique())


icon = Image.open("phonepe-logo-icon.png")
st.set_page_config(
    page_title="Phonepe Pulse Data Visualization | By SUNIL RAGAV",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': """# This dashboard app is created by *Sunil Ragav*!
                             Data has been cloned from Phonepe Pulse Github Repo"""}
)

st.sidebar.header(":wave: :violet[**Hello! Welcome to the dashboard**]")

with st.sidebar:
   selected = option_menu("Menu", ["Home","Charts & Explore Data","About"], 
                icons=["house","bar-chart-line", "exclamation-circle"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})


if selected == "Home":
    
    st.markdown("# :violet[Data Visualization and Exploration]")
    col1, col2 = st.columns([3, 2], gap="medium")
    with col1:
        st.markdown("### :violet[Domain :] Fintech")
        st.markdown("")
        st.markdown("### :violet[Technologies used :] Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.")
        st.markdown("")
        st.markdown("### :violet[Overview :] In this Streamlit web app, you can visualize the PhonePe Pulse data and gain insights on transactions, the number of users, top 10 states, districts, pin codes, and which brand has the most number of users, and so on. Bar charts, Pie charts, and Geo map visualization are used to provide insights.")

    with col2:
        st.image("phonepe-logo-icon.png")


if selected == "Charts & Explore Data":
    st.header("PhonePe Pulse Data Analysis📶")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        selected_state = st.selectbox(
            "Select the Quarter⬇️",
            Quarter,
            index=0
        )
    with col2:
        selected_year = st.selectbox(
            "Select the Year⬇️",
            years,
            index=0
        )
    st.title("Geo graph⬇️:")
    filtered_df = df1[(df1['Quarter'] == selected_state) & (df1["Year"] == selected_year)]
    geoselect = df44[(df44["Year"] == selected_year) & (df44["Quarter"] == selected_state)]
    geogroup = geoselect.groupby(["Year", "Quarter", "State"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    geo = px.choropleth(geogroup, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='State',
                        hover_data=["Transaction_amount", "Transaction_count"],
                        color_continuous_scale='Reds')
    geo.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(geo, use_container_width=True) 


    st.markdown("### Transaction Analysis💲💱")
    select=option_menu(None,["State Analysis","District Analysis","Yearly Analysis","OverAll"],orientation="horizontal",styles={"nav-link": {"font-size": "20px" ,"margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
    if select=="State Analysis":
        col1,col2=st.columns(2)
        with col1:
          
          stateselection=st.selectbox("select the state⬇️:",states,index=0)
          
          transactiontype_selection=st.selectbox("select the Transaction Type⬇️",Transaction_type,index=0)
          
          Quarterselection=st.selectbox("select the Quarter⬇️",Quarter,index=0)

          fortransaction=df3[(df3["State"]==stateselection) & (df3["Transaction_type"]==transactiontype_selection) & (df3['Quarter'] == Quarterselection)]
          grouped_df_Transaction= fortransaction.groupby(["State","Transaction_type","Quarter","Year","Transaction_amount"])["Transaction_count"].sum().reset_index()
          sorted_transc=grouped_df_Transaction.sort_values(by="Transaction_count",ascending=False)
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        newgr = px.bar(sorted_transc, x="Year", y="Transaction_count",hover_data="Transaction_amount",title=f"State selected is {stateselection}")
        st.plotly_chart(newgr, use_container_width=True) 

    if select=="District Analysis":
        col1 ,col2=st.columns(2)
        with col1:
          
          diststate=st.selectbox("select the State⬇️",states,index=0)
          
          disyear=st.selectbox("select the Year⬇️",years,index=0)
          
          disquarter=st.selectbox("select the Quarter⬇️",Quarter,index=0)
          
          districtselection=df4[(df4["State"]==diststate) & (df4["Year"]==disyear) & (df4['Quarter'] == disquarter)]          
          sorted_transc=districtselection.sort_values(by="Count",ascending=False)
          
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        districtanaly = px.bar(districtselection, x="District", y="Count",labels={"Count":"Total_Transaction_Count","Amount":"Total_amount"},color="District",hover_data="Amount",title=f"State of {diststate} got {len(districtselection)} districts")
        st.plotly_chart(districtanaly, use_container_width=True) 

    if select=="Yearly Analysis":
        col1 ,col2=st.columns(2)
        with col1:
          
          Typeselectionfordistrict=st.selectbox("Select the Type of Transaction⬇️",Transaction_type,index=0)
          
          Year_selectionfordistrict1=st.selectbox("select the Year⬇️",years,index=0)
          
          
          
          districtselection1 = df3[(df3["Transaction_type"] == Typeselectionfordistrict) & (df3["Year"] == Year_selectionfordistrict1)]         
          grouped_df_trans_year= districtselection1.groupby(["Year","Transaction_type","State"])[["Transaction_count","Transaction_amount"]].sum().reset_index()
          sorted_transc_year=grouped_df_trans_year.sort_values(by="Transaction_count",ascending=True)

          
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        districtanalyyear=px.bar(sorted_transc_year,x="State",y="Transaction_count",color="State",hover_data="Transaction_amount",title=f"Yearly Analysis of {Typeselectionfordistrict} in {Year_selectionfordistrict1} ")
        st.plotly_chart(districtanalyyear, use_container_width=True)

    if select=="OverAll":
      piee_df=df3.groupby(["Year"])["Transaction_count"].sum().reset_index()
      piee_df1=df3.groupby(["Year"])["Transaction_amount"].sum().reset_index()
      col1,col2=st.columns(2)
      with col1:
         piecha=px.pie(piee_df,values="Transaction_count",names="Year",hole=0.5,color_discrete_sequence=px.colors.sequential.Purp,title="Overall Transaction as Pie Chart")
         st.plotly_chart(piecha,use_container_width=True)
      with col2:
         piechaa=px.pie(piee_df1,values="Transaction_amount",names="Year",hole=0.5,color_discrete_sequence=px.colors.sequential.Purp,title="Overall Transaction as Pie Chart")
         st.plotly_chart(piechaa,use_container_width=True)






    st.markdown("### User Analysis💲💱")
    
    selects=option_menu(None,["State Analysis ","District Analysis ","Yearly Analysis ","OverAll "],orientation="horizontal",styles={"nav-link": {"font-size": "20px", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
    
    if selects=="State Analysis ":
        col1,col2=st.columns(2)
        with col1:
          statedropdownuser=st.selectbox("select the state⬇️ ",states,index=0)
          userstate=df5[(df5["State"])==statedropdownuser]
          userdist=userstate.groupby(["State","Year"])[["RegisteredUser","AppOpens"]].sum().reset_index()
          st.info("In this below Scatterplot the color variation on the plot indicates AppOpens and Registered Users in a specific or selected State")
          st.info("""
                    ##### Graph info:
                    - X-axis indicates Year.
                    - Y-axis indicates Values.""")
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        userdis=px.scatter(userdist,x="Year",y=["AppOpens","RegisteredUser"],title="Analysis of AppOpens and Registeredsers")
        userdis.update_traces(marker_size=20,marker_line_color="red",marker_symbol="circle")
        st.plotly_chart(userdis, use_container_width=True) 

    if selects=="District Analysis ":
        col1 ,col2=st.columns(2)
        with col1:
          
          selectedstateuser=st.selectbox("Select the State⬇️ ",states,index=0)
          
          selectedyearuser=st.selectbox("Select the Year⬇️ ",years,index=0)
          
          selectedquarteruser=st.selectbox("Select the Quarter⬇️ ",Quarter,index=0)
          
          userdistr = df5[(df5["State"] == selectedstateuser) & (df5["Year"] == selectedyearuser) & (df5["Quarter"] == selectedquarteruser)]
          
          

          
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        userdisapp=userdistr.groupby(["State","Year","Quarter","District","RegisteredUser"])["AppOpens"].sum().reset_index()
        userdisappres=userdistr.groupby(["State","Year","Quarter","District"])["RegisteredUser"].sum().reset_index()
        userapp=px.bar(userdisapp,x="District",y="AppOpens",title=f"State of {selectedstateuser} got {len(userdistr)} districts")
        userappres=px.bar(userdisappres,x="District",y="RegisteredUser",title=f"State of {selectedstateuser} got {len(userdistr)} districts")
        st.plotly_chart(userapp,use_container_width=True)
        st.plotly_chart(userappres,use_container_width=True)

    if selects=="Yearly Analysis ":
        col1 ,col2=st.columns(2)
        with col1:
          
          selectedstateuser1=st.selectbox("Select the State⬇️ ",states,index=0)
          
          selectedyearuser1=st.selectbox("Select the Year⬇️ ",years,index=0)
          userdistr1 = df6[(df6["State"] == selectedstateuser1) & (df6["Year"] == selectedyearuser1)]
          st.info("In this below Pie-plot,it explains the count of different kind of Mobile Brand Users")
          st.info("""
                    ###### Pie-plot info:
                    - Names indicates Brand.
                    - Values indicates Count.""")

          
          

          
        with col2:
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.


                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.


                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.


                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        userdisapp1=userdistr1.groupby(["State","Year","Quarter","Brand"])["count"].sum().reset_index()
        userapp1=px.pie(userdisapp1,names="Brand",values="count",color_discrete_sequence=px.colors.sequential.Purp,title="User Analysis with Mobile Details",hole=0.5)
        st.plotly_chart(userapp1, use_container_width=True)


    if selects=="OverAll ":
      
      useroverall=df5.groupby(["Year"])[["RegisteredUser","AppOpens"]].sum().reset_index()
      col1,col2=st.columns(2)
      with col1:
         userapp2=px.pie(useroverall,names="Year",values="AppOpens",title="Overall AppOpens Analysis")
         st.plotly_chart(userapp2,use_container_width=True)
         st.info("""
                 #### OverAll analysis:
                 - Here the Names holds Year.
                 - Therefore the Values holds AppOpens.
                 - Shows AppOpens as per year""")
      with col2:
         userapp3=px.pie(useroverall,names="Year",values="RegisteredUser",title="Overall Registered User Analysis")
         st.plotly_chart(userapp3,use_container_width=True)
         st.info("""
                 #### OverAll analysis:
                 - Here the Names holds Year.
                 - Therefore the Values holds RegisteredUser.
                 - Shows RegisteredUsers as per year""")
         
    st.title("RegisteredUser⬇️")
    col1,col2=st.columns(2)
    with col1:
       selectyear=st.select_slider("Select the year⬇️",years)
    with col2:
       selectquarter=st.select_slider("Select the quarter⬇️",Quarter)

    filtered_df = df1[(df1['Quarter'] == selectquarter) & (df1["Year"] == selectyear)]
    grouped_df_registereduser = filtered_df.groupby(["State", "Year"])["RegisteredUsers"].sum().reset_index()
    sorted_register=grouped_df_registereduser.sort_values(by="RegisteredUsers",ascending=False)
    life = px.bar(sorted_register, x="State", y="RegisteredUsers", color="State", hover_data="RegisteredUsers",title="Graph of RegisteredUsers:")
    st.plotly_chart(life,use_container_width=True)


    st.markdown("<h1 style='color: purple; text-align: center;'>Top 3 Information</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        chooseyear = st.selectbox("Select the Year⬇", years)

    with col2:
        choosequarter = st.selectbox("Select the Quarter⬇", Quarter)

    column1, column2, column3, column4 = st.columns(4)

    with column1:
        st.markdown("#### Top 3 Transaction Amount")
        group_df = df2[(df2['Quarter'] == choosequarter) & (df2["Year"] == chooseyear)]
        groups_df = group_df.groupby(['State', 'Year'])['Transaction_amount'].sum().reset_index()

        sortit = groups_df.sort_values(by="Transaction_amount", ascending=False)
        st.dataframe(sortit[["State", "Transaction_amount"]].head(3),use_container_width=True)

    with column2:
        st.markdown("#### Top 3 Transaction Count")
        group_df1 = df2[(df2['Quarter'] == choosequarter) & (df2["Year"] == chooseyear)]
        groups_df1 = group_df1.groupby(['State', 'Year'])['Transaction_count'].sum().reset_index()

        sortit = groups_df1.sort_values(by="Transaction_count", ascending=False)
        st.dataframe(sortit[["State", "Transaction_count"]].head(3),use_container_width=True)

    with column3:
        st.markdown("#### Top 3 Registered Users")
        group_df2 = df1[(df1['Quarter'] == choosequarter) & (df1["Year"] == chooseyear)]
        grouped_df_registereduser = group_df2.groupby(["State", "Year"])["RegisteredUsers"].sum().reset_index()

        sorted_register = grouped_df_registereduser.sort_values(by="RegisteredUsers", ascending=False)
        st.dataframe(sorted_register[["State", "RegisteredUsers"]].head(3),use_container_width=True)

    with column4:
        st.markdown("#### Top 3 App Opens")
        group_df3 = df5[(df5['Quarter'] == choosequarter) & (df5["Year"] == chooseyear)]
        userdisapp = group_df3.groupby(["State", "Year", "Quarter", "District"])["AppOpens"].sum().reset_index()

        sorted_appopen=userdisapp.sort_values(by="AppOpens",ascending=False)
        st.dataframe(sorted_appopen[["State", "AppOpens"]].head(3))


if selected == "About":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[About PhonePe Pulse:] ")
        st.write("##### BENGALURU, India, On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")
        
        st.write("##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")
        
        st.markdown("### :violet[About PhonePe:] ")
        st.write("##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")
        st.write("##### :violet[Dataset Github Repository Link]⬇️")
        st.write("https://github.com/PhonePe/pulse/tree/master/data")
        
        st.write("**:violet[My Project GitHub link]** ⬇️")
        st.write("https://github.com/SunilRagav99/phonepe-pluse-data-visualization")
        st.write("**:violet[Image and content source]** ⬇️")
        st.write("https://www.prnewswire.com/in/news-releases/phonepe-launches-the-pulse-of-digital-payments-india-s-first-interactive-geospatial-website-888262738.html")
        
    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        phonepee=Image.open(r"C:\Users\sunil\OneDrive\Desktop\python guvi\Untitled Folder\phonepe-logo-icon.png")
        st.image(phonepee)
