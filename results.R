results = read.csv('/Users/camstark/Documents/runscrape/melissas_results.csv', stringsAsFactors = FALSE)

seconds = strsplit(results$GUN.TIME, ":")

strsplit(results$GUN.TIME, ":")