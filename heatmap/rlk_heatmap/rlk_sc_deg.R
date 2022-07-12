#try to match the heatmap color with the legend color 
#figure out the color thing for heatmap two, maybe do the heatmap seperately


#load the deg data
rlk_sc_deg <- read.csv("./rlk_sc_deg.csv", header = TRUE)

rownames(rlk_sc_deg) <- rlk_sc_deg[,2]
rlk_sc_deg <- rlk_sc_deg[,-2]
rlk_sc_deg2 <-rlk_sc_deg[,-1]
df <- data.matrix(rlk_sc_deg)
df2 <- data.matrix(rlk_sc_deg2)
#df <- data.matrix(sapply(rlk_rp_deg[,c(2,3,4)],as.numeric))
domain1<-as.data.frame(df[,1])
domain2<-rlk_sc_deg[1]
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
png("./rlk_sc_euc_complete.png",
    width = 8*300,
    height = 23*300,
    res = 300,
    pointsize = 8)

library(ComplexHeatmap)
library(circlize)

col_fun = colorRamp2(c(-7,0,7), c("red", "black", "green"))
col_fun(seq(-1,1))


domain_type <- list(domain=c("1"="chocolate","2"="chartreuse","3"="cadetblue","4"="burlywood","5"="pink",
                             "6"="blue","7"="black","8"="beige","9"="firebrick", "10"="aquamarine","11"="seagreen",
                             "12"="darkviolet","13"="darkred","14"="darkgrey"))

                         
annot <- rowAnnotation(domain = df[,c(1)], col=domain_type, show_legend = FALSE)

col_fun_prop = c("chocolate","chartreuse","cadetblue","burlywood","pink",
                 "blue","black","beige","firebrick","aquamarine","seagreen","darkviolet","darkred","darkgrey")
lgd = Legend(legend_gp = gpar(fill=col_fun_prop), title = "domain",
             at = 1:14, labels=c("egf_wak","g-lectin-b","g-lectin-b/p/s","g-lectin-b/s",
                                 "g-lectin-p/s","l-lectin","lrr","lrr_malectin","lysm","malectin",
                                 "pr5k","rlk_or_rlck_only_pkinase","stress-antifung","wak"))
hm <- Heatmap(df[,c(2,3,4,5)], cluster_columns = FALSE, col = col_fun, show_row_dend = FALSE,
              row_km = 4, row_km_repeats = 100, cluster_row_slices = FALSE, 
              clustering_distance_rows = "euclidean", row_dend_reorder = TRUE,
              clustering_method_rows = "complete",
              right_annotation = annot,
              heatmap_legend_param = list(legend_direction = 'horizontal',legend_width = unit(5,"cm"), title = "")) 

draw(hm, auto_adjust = FALSE)
draw(lgd, draw(lgd, x = unit(0.85, "npc"), y = unit(0.3, "npc")))
#close the PNG device
dev.off()
