import DataHandling as DH

data = DH.LoadCSV('G:/Projects/Repos/data-vis-study/IncomeInequality.csv')

# output javascript to an html file
file = open("generatedMap.html", "w")

file.write("<html>\n")
file.write("  <head>\n")
file.write("    <script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script>\n")
file.write("    <script type=\"text/javascript\">\n")
file.write("      google.charts.load('current', {\n")
file.write("        'packages':['geochart'],\n")
file.write("        'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'\n")
file.write("      });\n")
file.write("      google.charts.setOnLoadCallback(drawRegionsMap);\n")
file.write("      function drawRegionsMap() {\n")
file.write("        var data = google.visualization.arrayToDataTable([\n")
file.write("          ['Country', 'Gini Index'],\n")

# now loop through and add this line
# ['Country', 'index'],

for i, (key, item) in enumerate(data.items.items()):
  if (item.values[1]):
    country = item.key
    value = item.values[0]
    if i == len(data.items)-1:
      # don't add comma if this is the last item in the dictionary
      file.write("          ['" + country + "', " + value + "]\n")
    else:
      file.write("          ['" + country + "', " + value + "],\n")

# output rest of code
file.write("        ]);\n")
file.write("        var options = {\n")
file.write("          colorAxis: {\n")
file.write("            colors: ['#00853f', '#ffff00', '#e31b23']\n")
file.write("          }\n")
file.write("        };\n")
file.write("        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));\n")
file.write("        chart.draw(data, options);\n")
file.write("      }\n")
file.write("    </script>\n")
file.write("  </head>\n")
file.write("  <body>\n")
file.write("    <div id=\"regions_div\" style=\"width: 900px; height: 500px;\"></div>\n")
file.write("  </body>\n")
file.write("</html>\n")
file.close()