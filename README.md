# NFT Price Tracker and Forecaster

![image](https://user-images.githubusercontent.com/99493522/164087329-d61dac3d-ec6f-4dfa-9896-13821a6bff06.png)


## Background 

NFTs (Non Fungible Tokens) are digital assets that are unique and represents real-world tangible objects like art, music, in-game items, videos, audio recording and photos. They can be bought and sold online using crypotcurrency like Ethereum (ETH) and are becoming increasingly popular. 
This project will create an NFT price tracker to compare and forecast NFT valuations to  provide recommendations for NFT investors, collectors and traders.  It will aggregate top NFT projects based on popularity and activity, and help new NFT investors decide which NFTs to purchase based on their risk tolerance. The following data will be considered;  daily prices, volume , life span of collection, rank and popularity, trends, and activity using OpenSea API.

Data for this project was retrieved from [OpenSea](https://opensea.io/), an API key was required and can be obtained here:
[Request OpenSea API]( https://docs.opensea.io/reference/request-an-api-key)

## Technology

* OpenSea API
* Alpaca API
* Python 
* Jupyter Notebook 
* Streamlit

## Resources

**OpenSea API:**

* [Asset Data](https://api.opensea.io/api/v1/assets) was used to get different assets for each NFT collection slug (ie. boredapeyachtclub) 

* [Asset Data Documentation](https://docs.opensea.io/reference/getting-assets)

* [Event Data ](https://api.opensea.io/api/v1/events) was used to get event data for any given asset. 

* [Event Data Documentation ](https://docs.opensea.io/reference/retrieving-asset-events)

[Alpaca API](https://api.alternative.me/v2/ticker/Ethereum/?convert=CAD) was used to get the current price of ETH. 


## Installations
This notebook needs to be executed in pyvizenv env to display all the images in panel and needs python-dotenv to load env variables, this can be done by activating the pyvizenv env and also loading the alpaca apis using commands below:

**conda activate pyvizenv**

**pip install python-dotenv**

## Usage Examples  

Data from the following NFT collections were obtained:
* Bored Ape Yacht Club
* Mutant Bored APe Yacht Club
* Cryptokitties
* Doodles-official
* Pudgy Penguins

The NFT Price Tracker will display randon  assests from each of the five collections, samples shown below. 

![boredapeyachtclub.png](Images/boredapeyachtclub.png)
![cryptokitties.png](Images/cryptokitties.png)
![doodles-official.png](Images/doodles-official.png)
![pudgypenguins.png](Images/pudgypenguins.png)


**Note:**
* NFTs can have multiple sales per day and there is no closing price. 
* An NFT collection can have different assets and the prices of the assets vary based on the rarity and/or features.
* For the sake of simplicity, we have treated all assets equally and the floor price is the lowest price of any of the assets sold on a particular day.
* Floor price was determined from the event data. 

**There are 2 options to determine the price of an NFT per day:**
1) Get average price of the NFT sold for a day, this was calculated by using the rollowing median to avoid the high fluctuations in the data. 
2) Get the floor price the NFT is sold on any particular day.

### Examples of NFT Price Tracker Visualizations (displayed using streamlit)
The floor price over a period of time for each of the 5 collections are displayed as a **line chart** as shown in the example below. 

![image](https://user-images.githubusercontent.com/99493522/164294432-0b0bf36b-6eb8-4dcf-8bde-fc7c50b94996.png)


Using the rolling median, the **Monte Carlo simulations** are generated for each NFT collections. The projection is based on 6 months of historical data and projected for a duration of 30 days as shown below. 


![image](https://user-images.githubusercontent.com/99493522/164294985-48114ac2-8136-4329-a662-e957963b83af.png)


## References 
* [UToronto BootCamp](https://utoronto.bootcampcontent.com/utoronto-bootcamp/UTOR-VIRT-FIN-PT-02-2022-U-LOL/-/blob/main/Units-Activities/05-APIs/Supplemental/AlpacaMarkets_Installation-Guide.md)
* https://github.com/zseta/python-opensea
* https://www.youtube.com/watch?v=ga4hTqNRjfw
* https://levelup.gitconnected.com/how-to-collect-nft-sales-data-using-opensea-api-5a6b9b163f7
* https://www.youtube.com/watch?v=-IM3531b1XU
* Chainalysis, January 2022; 2. Grayscale, November 2021; 3. KPMG, The new wave of Web 3.0, January 2022 

## Contributors

Chantal Garnett, Sameer Lakhe, Emiliano Mendez, Marcus Policicchio
