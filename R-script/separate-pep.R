library(Biostrings)

pep <- readAAStringSet("../all.pep")
batch <- cut(seq_along(pep),
             breaks = c(seq(0, length(pep), 10000),
                        length(pep)))

for(i in seq_along(levels(batch))){
  writeXStringSet(pep[batch == levels(batch)[i]],
                  paste0("../separate-pep/batch_", i, ".pep"))
}
