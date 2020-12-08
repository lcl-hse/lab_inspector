library(tidyverse)
# library(xlsx)  # uncooment if needed
library(stargazer)
# setwd('')  # set if needed


poisson_linear_model <- function(name){
  data <- read_csv(sprintf('./datasets/dataset_%s.csv', name), col_names = TRUE)
  data_1 <- read_csv(sprintf('./datasets/dataset_%s_1.csv', name), col_names = TRUE)
  data_2 <- read_csv(sprintf('./datasets/dataset_%s_2.csv', name), col_names = TRUE)

  data %>%
  select(-name) -> data

  data_1 %>%
  select(-name) -> data_1

  data_2 %>%
  select(-name) -> data_2
  
  
  fit <- glm(data = data, errors~., family = poisson)
  fit_1 <- glm(data = data_1, errors~., family = poisson)
  fit_2 <- glm(data = data_2, errors~., family = poisson)
  
  stargazer(fit_1, fit_2, fit, type='html',
            title="Regression Results",
            p.auto = TRUE,
            single.row=TRUE,
            ci=TRUE, ci.level=0.9,
            report='vscp*',
            out='regression_results.html')
  
  # This part creates xlsx tables with data

  # x <- summary(fit)
  # data.frame(x$coefficients[-1,]) %>% 
  #   select(Pr...z..) %>% 
  #   arrange(Pr...z..) %>% 
  #   `colnames<-`('p-value') %>% 
  #   write.xlsx(sprintf('%s_glm.xlsx', name))
  # 
  # 
  # x_1 <- summary(fit_1)
  # data.frame(x_1$coefficients[-1,]) %>% 
  #   select(Pr...z..) %>% 
  #   arrange(Pr...z..) %>% 
  #   `colnames<-`('p-value') %>% 
  #   write.xlsx(sprintf('%s_glm_1.xlsx', name))
  # 
  # 
  # x_2 <- summary(fit_2)
  # data.frame(x_2$coefficients[-1,]) %>% 
  #   select(Pr...z..) %>% 
  #   arrange(Pr...z..) %>% 
  #   `colnames<-`('p-value') %>% 
  #   write.xlsx(sprintf('%s_glm_2.xlsx', name))
}

poisson_linear_model('syntax')

# Loop for all data

# for(name in c('syntax', 'derivation', 'lexical_choice_verb_pattern',
#               'verb_morphology',
#               'writing_conventions')){
#   print(name)
#   linear_model(name)
#   poisson_linear_model(name)
# }