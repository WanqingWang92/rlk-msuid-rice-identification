#try to match the heatmap color with the legend color 
#figure out the color thing for heatmap two, maybe do the heatmap seperately


#load the deg data
rlk_rp_deg <- read.csv("./rlk_rp_deg.csv", header = TRUE)

rownames(rlk_rp_deg) <- rlk_rp_deg[,2]
rlk_rp_deg <- rlk_rp_deg[,-2]
df <- data.matrix(rlk_rp_deg)
#df <- data.matrix(sapply(rlk_rp_deg[,c(2,3,4)],as.numeric))
domain1<-as.data.frame(df[,1])
domain2<-rlk_rp_deg[1]
domain_merge <- merge(domain1, domain2,
                          by = 'row.names', all = TRUE)
domain_merge<-domain_merge[,-1]
domain_list <-unique(domain_merge)
colnames(domain_list) <- c("order","domain")
domain_sorted <- domain_list[order(domain_list$order),]
domain_list=as.list(domain_sorted['domain'])
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
png("./rlk_rp_euc_complete.png",
    width = 5*300,
    height = 25*300,
    res = 300,
    pointsize = 8)

library(ComplexHeatmap)
library(circlize)

col_fun = colorRamp2(c(-7,0,7), c("red", "black", "green"))
col_fun(seq(-1,1))

#domain <- as.data.frame(domain_list)
domain_type <- list(domain=c("1"="coral","2"="chocolate","3"="chartreuse","4"="cadetblue","5"="burlywood","6"="brown",
                             "7"="blue","8"="black","9"="beige","10"="aquamarine","11"="darkviolet","12"="darkred","13"="darkgrey"))

#annot<- rowAnnotation(sth = domain_list, col=domain_type, width = unit(5,"cm"))                           
annot <- rowAnnotation(domain = df[,c(1)], col=domain_type)

hm <- Heatmap(df[,c(2,3,4)], cluster_columns = FALSE, col = col_fun, show_row_dend = FALSE,
              row_km = 5, row_km_repeats = 100, cluster_row_slices = FALSE, 
              clustering_distance_rows = "euclidean", row_dend_reorder = TRUE,
              clustering_method_rows = "complete",
              right_annotation = annot,
              heatmap_legend_param = list(legend_direction = 'horizontal',legend_width = unit(5,"cm"), title = ""))




#hm <-Heatmap(df[,c(1)], width = unit(4, "mm"), col = structure(1:13), show_row_dend = FALSE,
#             show_heatmap_legend = FALSE, show_row_names = FALSE)

#ldg<-Legend(at=1:13,labels=domain_list$domain, name="domain",legend_gp = gpar(fill = 1:13))      
#draw(ldg, just = c("right", "bottom"))
draw(hm, auto_adjust = FALSE)

#close the PNG device
dev.off()
