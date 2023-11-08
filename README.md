This project has two parts:
1. Visualisation of co2 emissions and budget for areawise reduction of CO2 emissions
2. Dtermination of optimised warehouse locations

   
**Part-1**


**Introduction**
Welcome to the Supply Chain Sustainability Report project, a practical guide for calculating and visualizing CO2 emissions in your distribution network. 
This project is intended to assist organizations in addressing the growing demands for transparency in sustainable development from both investors and customers. 
The focus here is on the calculation of CO2 emissions, particularly Scope 3 emissions related to downstream transportation, providing a valuable resource for assessing and improving the environmental impact of your distribution network.

***Data Processing***
This project is structured into three core sections: data collection, data processing, and CO2 emission calculations. In the "Data Collection" section, you will find guidance on how to gather the essential datasets, including shipped order lines and unit of measure conversions. The "Data Processing" segment outlines the crucial steps for data cleaning, transformation, and organization, setting the stage for accurate CO2 emission calculations. By following these steps, you will be well-prepared to determine the carbon footprint of your supply chain.

***Visualization and Contribution***
To create impactful sustainability reports, this project guides you on using PowerBI for data visualization. This empowers you to craft informative reports effectively. Additionally, contributions from the open-source community are encouraged. If you're interested in enhancing or expanding this project, comprehensive guidelines for contributions, including pull requests and issue reporting, are available. This project adheres to an open-source license, making it a valuable tool for organizations looking to address investor and customer demands for sustainability transparency and make informed decisions regarding their supply chain's environmental impact.
**Part-2**


**Introduction and Purpose**

This project is designed to optimize warehouse locations for restaurants, aiming to enhance their supply chain efficiency. By leveraging a Weighted K-Means clustering approach, it helps restaurants make data-driven decisions on where to place their warehouses for more effective service to their customers. This solution considers various factors, such as customer demand, population density, and geographical location, to prioritize the optimal warehouse sites.

**Methodology and Optimization**

The project initiates by collecting relevant data, including restaurant locations, customer demand, and regional demographics. After preprocessing the data to obtain precise geographical coordinates, a Weighted K-Means algorithm is applied. This modified clustering algorithm accounts for factors like customer demand and delivery routes, weighting them appropriately to guide the selection of warehouse locations. Additionally, the Elbow Method is used to determine the optimal number of warehouses (K) for the restaurant's distribution network, reducing costs and improving delivery efficiency.

**How to Use and Contribution**

To utilize this optimization solution, simply clone the repository to your local machine and install the necessary dependencies, such as Python, NumPy, Pandas, Scikit-Learn, and Haversine for distance calculations. Then, run the primary script for the weighted K-Means clustering analysis. 
