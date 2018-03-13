To retrieve the data from url, the module urllib is used.
In order to parse json data, the json library is also imported.
The url is get from the user as an input. Then the data in the url is decoded through json.loads function.
Now an empty set is created.
Using a for loop, the investors which are separated by 'and' is replaced by ',' and the next line will split the names individually which contains comma (',').
Again a for loop is used to remove the spaces in the left side using lstrip() and right side using rstrip() and a strip('\n') function to remove the '\n' which are present in the data.
Now the corrected data will be added to the set using union function. Next an array is created to store the investors with the product.
Then using a for loop, for every episode, first the investor is stored in a variable and then using the investor name, the product is appended with the investor name in an array removing the left space, right space and '\n'.
Using a for loop, the array is sorted using the length of the array and then the investor with maximum product is printed first and then the investor with second maximum products is printed second and goes on.
