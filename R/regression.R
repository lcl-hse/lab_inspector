library(tidyverse)
library(xlsx)
library(stargazer)
setwd('C:/Users/anton/–абочий стол/лаба показатели сложности')

# linear_model <- function(name){
# data <- read_csv(sprintf('./datasets/dataset_%s_lr.csv', name), col_names = FALSE)
# data_1 <- read_csv(sprintf('./datasets/dataset_%s_lr_1.csv', name), col_names = FALSE)
# data_2 <- read_csv(sprintf('./datasets/dataset_%s_lr_2.csv', name), col_names = FALSE)
# 
# row_data <- read_csv(sprintf('./datasets/dataset_%s.csv', name), col_names = FALSE)
# rows <- c('Intercept', row_data$X1)
# 
# colnames(data) <- rows
# colnames(data_1) <- rows
# colnames(data_2) <- rows
# 
# fit <- lm(data = data, Intercept~.)
# fit_1 <- lm(data = data_1, Intercept~.)
# fit_2 <- lm(data = data_2, Intercept~.)
# 
# 
# x <- summary(fit)
# data.frame(x$coefficients[-1,]) %>% 
#   select(Pr...t..) %>% 
#   arrange(Pr...t..) %>% 
#   `colnames<-`('p-value') %>% 
#   write.xlsx(sprintf('%s_lm.xlsx', name))
# 
# 
# x_1 <- summary(fit_1)
# data.frame(x_1$coefficients[-1,]) %>% 
#   select(Pr...t..) %>% 
#   arrange(Pr...t..) %>% 
#   `colnames<-`('p-value') %>% 
#   write.xlsx(sprintf('%s_lm_1.xlsx', name))
# 
# 
# x_2 <- summary(fit_2)
# data.frame(x_2$coefficients[-1,]) %>% 
#   select(Pr...t..) %>% 
#   arrange(Pr...t..) %>% 
#   `colnames<-`('p-value') %>% 
#   write.xlsx(sprintf('%s_lm_2.xlsx', name))
# }

poisson_linear_model <- function(name){
  data <- read_csv(sprintf('./datasets/dataset_%s_lr.csv', name), col_names = FALSE)
  data_1 <- read_csv(sprintf('./datasets/dataset_%s_lr_1.csv', name), col_names = FALSE)
  data_2 <- read_csv(sprintf('./datasets/dataset_%s_lr_2.csv', name), col_names = FALSE)
  
  row_data <- read_csv(sprintf('./datasets/dataset_%s.csv', name), col_names = FALSE)
  rows <- c('Errors', row_data$X1)
  
  colnames(data) <- rows
  colnames(data_1) <- rows
  colnames(data_2) <- rows
  
  
  fit <- glm(data = data, Errors~., family = poisson)
  fit_1 <- glm(data = data_1, Errors~., family = poisson)
  fit_2 <- glm(data = data_2, Errors~., family = poisson)
  
  stargazer(fit_1, fit_2, fit, type='html',
            title="Regression Results",
            p.auto = TRUE,
            single.row=TRUE,
            ci=TRUE, ci.level=0.9,
            report='vscp*')
  
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

for(name in c('syntax', 'derivation', 'lexical_choice_verb_pattern',
              'verb_morphology',
              'writing_conventions')){
  print(name)
  linear_model(name)
  poisson_linear_model(name)
}
