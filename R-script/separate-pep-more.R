library(Biostrings)

pep <- readAAStringSet("../all.pep")
batch <- cut(seq_along(pep),
             breaks = c(seq(0, length(pep)-6338, 5000),
                        length(pep)))

for(i in seq_along(levels(batch))){
  writeXStringSet(pep[batch == levels(batch)[i]],
                  paste0("../separate-pep-more/batch_", i, ".pep"))
}
