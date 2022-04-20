import streamlit as st
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from dotenv import load_dotenv

st.sidebar.write("Navigate Here")
select = st.sidebar.selectbox("Use dropdown arrow to navigate",('Welcome','About Project','NFT Price Predictor','NFT Comparison'))

if select == 'Welcome':
    st.title("NFT Price Tracker")
    st.header("Welcome to the NFT Price Tracker Dashboard! Here you can learn about NFTs and receive in sight on short term prediction! Feel free to use the dropdown menu on the left to navigate this app")
    st.image("nft.jpg")
    st.write("Contributors: Chantal Garnett, Sameer Lakhe, Marcus Policicchio, Emiliano")
    st.write("University of Toronto FinTech Boot-Camp: Project 1 -  April 18, 2022")

if select == 'About Project':
    st.title(select)
    st.subheader("What is an NFT?")
    st.write('- A digital asset that is unique and represents real-world tangible objects like art, music, in-game items, videos, audio recording and photos.')
    st.write("- Bought and sold online, with cryptocurrency on specialized market-places like OpenSea.")
    st.write("- Exchanged in the Ethereum (ETH) blockchain.")
    st.write("- A digital certificate of authenticity.")
    
    st.subheader("Background and Motivation")
    st.subheader("NFTs Represent an emerging growth ecosystem")
    st.write("- NFTs have skyrocketed in popularity over the last year; 3,200 active collections in OpenSea at the end of 2021; 193 at the beginning of March 2020")
    st.write("- NFTs are an important element of the Metaverse; It is estimated that bringing the Metaverse to life may represent $1 Trillion USD in annual revenues; It is expected that Gen Z will be the main driver of early adoption of Web 3.0/Metaverse.")
    st.write("- NFTs are retail-driven; It is quite concentrated with the top 95 collections representing half of all NFT flips on OpenSea.")

    st.subheader("The NFT Price Tracker")
    st.write("Meet our typical user, John: A young professional who has $10 000 CAD to invest in the new emerging volatile market of NFTs. However, John knows very little about NFTs and even less about where to begin. His preliminary research has not led him very far.")
    st.write("There is a need for: An interactive platform designed for the novice investor, trader or collector to understand the NFT market; Providing information on trends, sales, recommendations on when, how and if to purchase or sell new and established collections ")
    st.write("The NFT Price Tracker will:")
    st.write("- Track and predict future NFT prices for 30 days based on average prices for 5 popular NFT collections over  6-months. ")
    st.write("- Calculate the amount of ETH needed to purchase a particular NFT collection. ")
    st.write("- Compare and forecast NFT  valuations. ")
    st.write("- Show the total number of sales for each collection.")
    st.write("- Identify  top NFT projects based on popularity and activity, to help new NFT investors and traders decide which collections to purchase based on their risk tolerance.")

    st.subheader("Key Questions")
    st.write("Question: Which NFT projects offer the best risk / reward ratio? ")
    st.write(" - Data Source: OpenSea API Alpaca API")
    st.write(" - Tool Used: APIs Python Monte Carlo simulation")
    st.write("Question: How can we predict the future price of an NFT collection?")
    st.write(f" - Data Source: NFT floor prices were pulled from various top NFT collections using the collection ‘slug’.Data sourced from OpenSea API.")
    st.write(" - Tool Used: APIs Python Monte Carlo simulation")
    st.write("Question: How can I visually compare price performance of various NFT collections?")
    st.write(" - Data Source: OpenSea API")
    st.write(" - Tool Used: APIs Python  PyViz for visualization IPython.display Streamlit")

    st.subheader("Challenges & Mitigants")
    st.write("Challenge: A Metamask wallet with non-zero Eth balance was required. Accessing the data from OpenSea. Mitigants: Submitted three different API requests to OpenSea early in the process to minimize risk of not receiving the key. Ensured an active metamask wallet with Eth was available.")
    st.write("Challenge: Insufficient data from some NFT collections. Mitigants: Collections within the top 25 most popular NFTs with the longest price history available were used.")
    st.write("Challenge: Some collections have significant price volatility which impacts the Monte Carlo Simulations. Mitigants: Manual adjustments and data cleanup were required.Used average daily price to show trends over time.Used rolling median  to show Monte carlo Simulations")
    st.write("Challenge: Making the data accessible to the end user. Mitigants: Stremlit to display charts and data in a user friendly and interactive manner.")    

    st.image("data.jpg")

    st.subheader("Next Steps:")
    st.write("Project 2")
    st.write("- Host the notebook on AWS cloud.")
    st.write("- Compare different NFT collections: User will be able to input a specific collection and/or select from a list to obtain statistics.")
    st.write("- More collections and visualizations will be added to the tracker.")
    st.write("- Ask user for risk tolerance and provide output based on sharpe ratio.")
    st.write("- Provide steps to purchasing an NFT.")
    st.write("Project 3")
    st.write("- Social media analysis (ie. twitter for NFT projects to get sentiment analysis).")
    st.write("- Check for explosive growth and categorize them with potential profitability.")
    st.write("- Alerts-identify dips and recommend buy/sell")
    st.write("- Alerts: Indicator of when prices increase or decrease")
    st.write("- Explore addition of NFT rarities into the model")   
    st.write("- Create an NFT ") 
    st.write("- Tracker will be offered as part of an incentive to purchasing an NFT.") 

if select == 'NFT Price Predictor':
    st.title(select)
    nft_select = st.selectbox("Select an NFT Project",('Bored Ape Yacht Club','Mutant Ape Yacht Club','Doodles','Crypto Kitties','Pudgy Penguins'))
    if nft_select == 'Bored Ape Yacht Club':
        st.image("boredapeyachtclub.png")
        massage_df = pd.read_csv('BAYCfinal.csv')
        massage_df = massage_df[['event_date','close']]   
        baycdf = pd.read_csv('BAYCclose.csv')
        baycdf = baycdf.set_index('event_date')
        baycdf = baycdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
        bayc_raw = pd.read_csv("boredapeyachtclub.csv") 
       # fig = px.line(baycdf,title="Average Daily Price(ETH) of Bored Ape Yacht Club")
        st.subheader("Average Daily Price(ETH) of Bored Ape Yacht Club")
        fig = px.line(baycdf)

        st.write(fig)

        st.subheader("Price Prediction Over The Next 30 Days")
        st.write("- Calculated using Monte Carlo simulations")
        st.write("- Price is shown the percentage change of the asset")        
        st.image("BAYC SIM.png")
        st.write("")
        st.write(f"- There is a 95% probability that the price of this NFT collection will range between a 34% decrease and 91% increase.") 

        #st.subheader("Distribution Plot")
        #st.image("BAYC dist.png")
        
        st.subheader("Average Daily Price(ETH)")
        st.dataframe(massage_df)

        st.subheader("Sample of Raw Data Collected Using Opensea API")
        st.dataframe(bayc_raw)        

    if nft_select == 'Doodles':
        st.image("doodles-official.png")
        massage_df = pd.read_csv('doodlesclose.csv')
        massage_df = massage_df[['event_date','close']]   
        doodlesdf = pd.read_csv('doodlesclose.csv')
        doodlesdf = doodlesdf.set_index('event_date')
        doodlesdf = doodlesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
        doodles_raw = pd.read_csv("doodles.csv")
        st.subheader("Average Daily Price(ETH) of Doodles")         
        fig = px.line(doodlesdf)

        st.write(fig)

        st.subheader("Price Prediction Over The Next 30 Days")
        st.write("- Calculated using Monte Carlo simulations")
        st.write("- Price is shown the percentage change of the asset")    
        st.image("doodles SIM.png")
        st.write(f"- There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 249% increase.") 

        #st.subheader("Distribution Plot")
        #st.image("doodles-official_dist_plot.png")

        st.subheader("Average Daily Price(ETH)")
        st.dataframe(massage_df)  

        st.subheader("Sample of Raw Data Collected Using Opensea API")
        st.dataframe(doodles_raw)
        
           

    if nft_select == 'Crypto Kitties':
        st.image("cryptokitties.png")
        massage_df = pd.read_csv('cryptokittiesclose.csv')
        massage_df = massage_df[['event_date','close']]   
        cryptokittiesdf = pd.read_csv('cryptokittiesclose.csv')
        cryptokittiesdf = cryptokittiesdf.set_index('event_date')
        cryptokittiesdf = cryptokittiesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
        cryptokitties_raw = pd.read_csv("cryptokitties.csv") 
        st.subheader("Average Daily Price(ETH) of Crypto Kitties")         
        fig = px.line(cryptokittiesdf)

        st.write(fig)

        st.subheader("Price Prediction Over The Next 30 Days")
        st.write("- Calculated using Monte Carlo simulations")
        st.write("- Price is shown the percentage change of the asset")    
        st.image("cryptokitties sim.png")
        st.write(f"- There is a 95% probability that the price of this NFT collection will range between 0 and 74% increase.") 
        #st.subheader("Distribution Plot")
        #st.image("cryptokitties dist.png")
        st.subheader("Average Daily Price(ETH)")
        st.dataframe(massage_df)         

        st.subheader("Sample of Raw Data Collected Using Opensea API")
        st.dataframe(cryptokitties_raw)
        


    if nft_select == 'Mutant Ape Yacht Club':
        st.image("mutant_ape_yatch_club.png")
        massage_df = pd.read_csv('mutantclose.csv')
        massage_df = massage_df[['event_date','close']]   
        mutantdf = pd.read_csv('mutantclose.csv')
        mutantdf = mutantdf.set_index('event_date')
        mutantdf = mutantdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
        mutant_raw = pd.read_csv("mutant.csv") 
        st.subheader("Average Daily Price(ETH) of Mutant Ape Yacht Club")         
        fig = px.line(mutantdf)

        st.write(fig)

        st.subheader("Price Prediction Over The Next 30 Days")
        st.write("- Calculated using Monte Carlo simulations")
        st.write("- Price is shown the percentage change of the asset")    
        st.image("mutant SIM.png")
        st.write(f"- There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 126% increase.") 

       # st.subheader("Distribution Plot")
       # st.image("mutant-ape-yacht-club_dist_plot.png")

        st.subheader("Average Daily Price(ETH)")
        st.dataframe(massage_df) 

        st.subheader("Sample of Raw Data Collected Using Opensea API")
        st.dataframe(mutant_raw)
        


    if nft_select == 'Pudgy Penguins':
        st.image("pudgypenguins.png")
        massage_df = pd.read_csv('pudgypenguinsclose.csv')
        massage_df = massage_df[['event_date','close']]   
        pudgypenguinsdf = pd.read_csv('pudgypenguinsclose.csv')
        pudgypenguinsdf = pudgypenguinsdf.set_index('event_date')
        pudgypenguinsdf = pudgypenguinsdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
        pudgypenguins_raw = pd.read_csv("pudgypenguins.csv") 
        st.subheader("Average Daily Price(ETH) of Pudgy Penguins")         
        fig = px.line(pudgypenguinsdf)

        st.write(fig)
        st.subheader("Price Prediction Over The Next 30 Days")
        st.write("- Calculated using Monte Carlo simulations")
        st.write("- Price is shown the percentage change of the asset")    
        st.image("pudgypenguins SIM.png")
        st.write(f"- There is a 95% probability that the price of this NFT collection will range between a 86% decrease and 225% increase.")         

        #st.subheader("Distribution Plot")
        #st.image("pudgypenguins_dist_plot.png")
        st.subheader("Average Daily Price(ETH)")
        st.dataframe(massage_df)         

        st.subheader("Sample of Raw Data Collected Using Opensea API")
        st.dataframe(pudgypenguins_raw)
        


if select == 'NFT Comparison':
    st.title("Compare NFT Price History & Predictions")
    summary = pd.read_csv("Summary.csv")
    st.dataframe(summary)
    col1, col2= st.columns(2)
    with col1:
        nft_select = st.selectbox("Select Project One",('Bored Ape Yacht Club','Mutant Ape Yacht Club','Doodles','Crypto Kitties','Pudgy Penguins'))
        if nft_select == 'Bored Ape Yacht Club':
            baycdf = pd.read_csv('BAYCclose.csv')
            baycdf = baycdf.set_index('event_date')
            baycdf = baycdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(baycdf,title="Price History of Bored Ape Yacht Club")
            st.write(fig) 
            st.image("BAYC SIM.png")
            st.image("BAYC dist.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 34% decrease and 91% increase.")

        if nft_select == 'Mutant Ape Yacht Club':
            mutantdf = pd.read_csv('mutantclose.csv')
            mutantdf = mutantdf.set_index('event_date')
            mutantdf = mutantdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(mutantdf,title="Price History of Mutant Ape Yacht Club")
            st.write(fig)
            st.image("mutant SIM.png")
            st.image("mutant-ape-yacht-club_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 126% increase.")

        if nft_select == 'Doodles':
            doodlesdf = pd.read_csv('doodlesclose.csv')
            doodlesdf = doodlesdf.set_index('event_date')
            doodlesdf = doodlesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(doodlesdf,title="Price History of Doodles")
            st.write(fig)
            st.image("doodles SIM.png")
            st.image("doodles-official_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 249% increase.") 


        if nft_select == 'Crypto Kitties':
            cryptokittiesdf = pd.read_csv('cryptokittiesclose.csv')
            cryptokittiesdf = cryptokittiesdf.set_index('event_date')
            cryptokittiesdf = cryptokittiesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(cryptokittiesdf,title="Price History of Crypto Kitties")
            st.write(fig)
            st.image("cryptokitties sim.png")
            st.image("cryptokitties dist.png")
            st.write(f"- There is a 95% probability that the price of this NFT collection will range between 0 and 74% increase.")  


        if nft_select == 'Pudgy Penguins':
            pudgypenguinsdf = pd.read_csv('pudgypenguinsclose.csv')
            pudgypenguinsdf = pudgypenguinsdf.set_index('event_date')
            pudgypenguinsdf = pudgypenguinsdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(pudgypenguinsdf,title="Price History of Pudgy Penguins")
            st.write(fig)
            st.image("pudgypenguins SIM.png")
            st.image("pudgypenguins_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 86% decrease and 225% increase.")



    with col2:
        nft_select2 = st.selectbox("Select Project Two",('Bored Ape Yacht Club','Mutant Ape Yacht Club','Doodles','Crypto Kitties','Pudgy Penguins'))
        if nft_select2 == 'Bored Ape Yacht Club':
            baycdf = pd.read_csv('BAYCclose.csv')
            baycdf = baycdf.set_index('event_date')
            baycdf = baycdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(baycdf,title="Price History of Bored Ape Yacht Club")
            st.write(fig) 
            st.image("BAYC SIM.png")
            st.image("BAYC dist.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 34% decrease and 91% increase.")

        if nft_select2 == 'Mutant Ape Yacht Club':
            mutantdf = pd.read_csv('mutantclose.csv')
            mutantdf = mutantdf.set_index('event_date')
            mutantdf = mutantdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(mutantdf,title="Price History of Mutant Ape Yacht Club")
            st.write(fig)
            st.image("mutant SIM.png")
            st.image("mutant-ape-yacht-club_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 126% increase.")

        if nft_select2 == 'Doodles':
            doodlesdf = pd.read_csv('doodlesclose.csv')
            doodlesdf = doodlesdf.set_index('event_date')
            doodlesdf = doodlesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(doodlesdf,title="Price History of Doodles")
            st.write(fig)
            st.image("doodles SIM.png")
            st.image("doodles-official_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 28% decrease and 249% increase.") 


        if nft_select2 == 'Crypto Kitties':
            cryptokittiesdf = pd.read_csv('cryptokittiesclose.csv')
            cryptokittiesdf = cryptokittiesdf.set_index('event_date')
            cryptokittiesdf = cryptokittiesdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(cryptokittiesdf,title="Price History of Crypto Kitties")
            st.write(fig)
            st.image("cryptokitties sim.png")
            st.image("cryptokitties dist.png")
            st.write(f"- There is a 95% probability that the price of this NFT collection will range between 0 and 74% increase.") 


        if nft_select2 == 'Pudgy Penguins':
            pudgypenguinsdf = pd.read_csv('pudgypenguinsclose.csv')
            pudgypenguinsdf = pudgypenguinsdf.set_index('event_date')
            pudgypenguinsdf = pudgypenguinsdf.rename(columns={'event_date':'Date','close':'Price in ETH'})
            fig = px.line(pudgypenguinsdf,title="Price History of Pudgy Penguins")
            st.write(fig)
            st.image("pudgypenguins SIM.png")
            st.image("pudgypenguins_dist_plot.png")
            st.write(f"There is a 95% probability that the price of this NFT collection will range between a 86% decrease and 225% increase.")
        
     