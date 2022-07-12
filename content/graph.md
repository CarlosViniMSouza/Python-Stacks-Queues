## Sample Data: Road Map of the United Kingdom

Once you ‘ve installed the required libraries, you’ll read a **weighted** and **undirected** graph of the [cities in the United Kingdom](https://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom) from a DOT file, which you can find in the accompanying materials:

This graph has 70 nodes representing UK cities and 137 edges weighted by the estimated distance in miles between the connected cities:

![img-England](https://files.realpython.com/media/roadmap.b8238a1b1c8c.png)

Note that the graph depicted above is a simplified model of the road network in the UK, as it doesn’t account for the road types, their capacity, speed limits, traffic, or bypasses.

Next up, you’ll use the networkx library to read this graph into Python.
