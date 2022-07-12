#try to match the heatmap color with the legend color 
#figure out the color thing for heatmap two, maybe do the heatmap seperately


#load the deg data
rlp_rp_deg <- read.csv("./rlp_rp_deg.csv", header = TRUE)

rownames(rlp_rp_deg) <- rlp_rp_deg[,2]
rlp_rp_deg <- rlp_rp_deg[,-2]
rlp_rp_deg2 <-rlp_rp_deg[,-1]
df <- data.matrix(rlp_rp_deg)
df2 <- data.matrix(rlp_rp_deg2)
#df <- data.matrix(sapply(rlk_rp_deg[,c(2,3,4)],as.numeric))
domain1<-as.data.frame(df[,1])
domain2<-rlp_rp_deg[1]
domain_merge <- merge(domain1, domain2,
                      by = 'row.names', all = TRUE)
domain_merge<-domain_merge[,-1]
domain_list <-unique(domain_merge)
colnames(domain_list) <- c("order","domain")
domain_sorted <- domain_list[order(domain_list$order),]

#install packages for clustering 
#package_list <- c("gplots", "factoextra", "NbClust")
#install.packages(package_list)

#k-means clustering
library(gplots)
library(factoextra)
library(NbClust)

scaled<- scale(df2)


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
png("./rlp_rp_euc_complete.png",
    width = 8*300,
    height = 5*300,
    res = 300,
    pointsize = 8)

library(ComplexHeatmap)
library(circlize)

col_fun = colorRamp2(c(-4,0,4), c("red", "black", "green"))
col_fun(seq(-1,1))


domain_type <- list(domain=c("1"="blue","2"="black","3"="aquamarine","4"="darkgrey"))


annot <- rowAnnotation(domain = df[,c(1)], col=domain_type, show_legend = FALSE)

col_fun_prop = c("blue","black","aquamarine","darkgrey")
lgd = Legend(legend_gp = gpar(fill=col_fun_prop), title = "domain",
             at = 1:4, labels=c("l-lectin","lrr","malectin","wak"))
hm <- Heatmap(df[,c(2,3,4)], cluster_columns = FALSE, col = col_fun, show_row_dend = FALSE,
              row_km = 6, row_km_repeats = 100, cluster_row_slices = FALSE, 
              clustering_distance_rows = "euclidean", row_dend_reorder = TRUE,
              clustering_method_rows = "complete",
              right_annotation = annot,
              heatmap_legend_param = list(legend_direction = 'horizontal',legend_width = unit(5,"cm"), title = "")) 

draw(hm, auto_adjust = FALSE)
draw(lgd, draw(lgd, x = unit(0.85, "npc"), y = unit(0.3, "npc")))
#close the PNG device
dev.off()
