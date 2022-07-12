#load the deg data
experiment3_deg <- read.csv("./rlk_rp_deg.csv", header = TRUE)

rownames(experiment3_deg) <- experiment3_deg[,2]
experiment3_deg <- experiment3_deg[,-c(1,2)]
df <- data.matrix(sapply(experiment3_deg,as.numeric))
rownames(df) <- rownames(experiment3_deg)

#install packages for clustering 
#package_list <- c("gplots", "factoextra", "NbClust")
#install.packages(package_list)

#k-means clustering
library(gplots)
library(factoextra)
library(NbClust)

scaled<- scale(df)


# Elbow method
fviz_nbclust(scaled, kmeans, method = "wss") +
  labs(subtitle = "Elbow method")

# Silhouette method
fviz_nbclust(scaled, kmeans, method = "silhouette")+
  labs(subtitle = "Silhouette method")

# Gap statistic
# nboot = 50 to keep the function speedy. 
# recommended value: nboot= 500 for your analysis.
# Use verbose = FALSE to hide computing progression.
set.seed(123)
fviz_nbclust(scaled, kmeans, nstart = 25,  method = "gap_stat", nboot = 500)+
  labs(subtitle = "Gap statistic method")


#create PNG for the heatmap
png("./heatmap_num_only.png",
    width = 5*300,
    height = 25*300,
    res = 300,
    pointsize = 8)

library(ComplexHeatmap)
library(circlize)
col_fun = colorRamp2(c(-5,0,5), c("red", "black", "green"))
col_fun(seq(-6,6))

hm <- Heatmap(df, cluster_columns = FALSE, col = col_fun, show_row_dend = FALSE,
              row_km = 5, row_km_repeats = 100, cluster_row_slices = FALSE, 
              clustering_distance_rows = "pearson", row_dend_reorder = TRUE,
              heatmap_legend_param = list(legend_direction = 'horizontal',
                                          legend_width = unit(5,"cm"),
                                          title = ""))

draw(hm, heatmap_legend_side = "top")

#close the PNG device
dev.off()


