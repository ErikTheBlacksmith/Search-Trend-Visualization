library(shiny)
library(ggplot2)
library(reticulate)
#use_python("filepath/python.exe")

PYTHON_DEPENDENCIES = c('pip', 'pytrends','pandas')
source_python("trends.py")

ui <- fluidPage(
  fluidRow(
    sidebarPanel(
      textInput("terms",label = "Enter terms (separated by ',')",value = "one,two,three ")
    ),
    sidebarPanel(
      dateRangeInput("date", label = "Date Range", start = "2022-01-01")
    )
    
  ),
  
  submitButton(text = "Apply Changes"),
  
  plotOutput("plot"),
  downloadButton("csvDown", "Download as .csv"),
    
    
)

server <- function(input, output){
  
 
  
  
  vecTerms <- reactive({
    strsplit(input$terms,',')[[1]]
  })
  
  graphFrame <- reactive({
    dfList = interestOverTime(terms = vecTerms(),
                              Tstart = as.character(input$date[1]), Tend = as.character(input$date[2]))
    if(length(dfList) != 1){
      baseV <- dfList[[1]][2]
      out <- dfList[[1]][1:2]
      for(df in dfList){
        scale <- baseV/df[2]
        out <- cbind(out,df[3:ncol(df)]*c(scale))
        
      }
    } else{
      out <- dfList[[1]]
    }
    out
  })
  
  output$plot <- renderPlot({
    
    out <- graphFrame()
    graphData <- data.frame(x = out[[1]],
                            y = c(out[2:ncol(out)], use.names = FALSE, recursive = TRUE),
                            group = as.vector(sapply(names(out)[2:length(names(out))],function(a){rep(a,nrow(out))})))
    ggplot(graphData, mapping = aes(x,y,color=group)) + geom_line()
  })
  
  
  
  output$csvDown <- downloadHandler(filename = "trendData.csv",content = function(file){write.csv(graphFrame(), file, row.names = FALSE)})
}

shinyApp(ui = ui, server = server)