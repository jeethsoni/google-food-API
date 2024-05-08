# Google Food API
**Author - Jeet Soni**

**Date - March 6, 2024**

---

### **Description**

Discover a personalized search API designed specifically for food items. Simply input the name of the food item you're interested in, and watch as it effortlessly populates an Excel sheet with the item's name, website link, author details, and a brief description.

### **How does it work?**

* I set up my Google developer account, created an `API key`, and enabled the custom search API. I also created my custom search programmable engine and grabbed the `CX` ID. 

* In my `main.py`, I defined a function called `custom_search` with a `search` parameter. I loaded the API Key from my `.env` file and built a service object to interact with Google using the `build` service that Google provides. Then, I called the `list` method on `service.cse`, passed the `search` and `CX ID` to search on my custom search engine, and returned the result.

* I called the `custom_search` function and passed the `search` variable into my main function. I stored the results as `JSON` file. 

* Python parser searches Google API and exports JSON data into an excel spreadsheet.

This is how the magic happens 😄

### **What if I want to run it?**

Here are the steps to run on your computer: 

* Go to https://console.cloud.google.com/projectselector2/apis/credentials?authuser=2&supportedpurview=project to grab your `API key.`

* Enable your custom search API here - https://console.cloud.google.com/marketplace/product/google/customsearch.googleapis.com

* Create your custom search engine here at https://programmablesearchengine.google.com/controlpanel/all and grab your `CX ID`

* Clone this git repository to your local machine. 

* Insert API Key and CX ID into `.env` file and viola, you are all set to run the program.

### **Conclusion**

While on a path to learning RESTful APIs, this was a fun little side project that showed me the magic of APIs and why it's really useful and essential. Doing this project also showed me an insight into how APIs work and how you can achieve a lot using APIs. 









