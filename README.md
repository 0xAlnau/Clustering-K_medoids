# K-Medoids amb Python
## Introducció
Aquest projecte personal ha sigut desenvolupat amb Python i per a que funcioni amb Linux. La finalitat d'aquest és la de poder realitzar Clustering sobre un conjunt de dades (llocs amb coordenades x,y) amb l'algorisme de `K-medoids`.

## K-medoids
Aquest algorisme és un de molts que es poden utilitzar per a realitzar clústers, com per exemple K-means. Aquest té l'avantatge de que és més resistent contra outliers en les dades, i també permet utilitzar diferents formes de calcular distàncies si es cau. Un medoid és una dada d'un clúster que minimitza la distància entre la resta de punts del clúster (està al mig del clúster dit de mala forma).

L'algorisme de K-medoids utilitza per dintre l'algorisme de Partitioning Around Medoids (PAM) clàssic. S'ha utilitzat una selecció aleatòria dels medoids inicials, i després, amb l'algorisme PAM es van provant swaps entre medoids i punts normals per a veure si el cost global entre tots els clústers disminueix (els medoids estan millor col·locats a cada clúster). El càlcul de la distància entre tots els punts s'ha fet amb la distància tradicional Euclidia.

## Execució
Per a executar el programa només cal fer: `python3 input_cluster.py`  

Si es vol utilitzar un fitxer de la carpeta `Inputs` cal fer: `python3 input_cluster.py < Inputs/input-42llocs-4clusters.txt`  

Els tres fitxers més rellevants són:
- `input_cluster.py`: aquest arxiu és el que interactua amb l'usuari, i li permet decidir si vol introduir els llocs a mà o des de un arxiu .csv. Una vegada ja té totes les dades d'entrada se les passa a l'algorisme de Clustering.
- `cluster_k_medoids.py`: aquí s'implementa tot el Clustering, rep els llocs a tractar, quants hi ha i quants clústers es volen.
- `Lloc.py`: és una classe que permet representar les dades. Un lloc té un nom i una coordenada x i una altra y. Els llocs s'han de visualitzar com una vista de satèl·lit.

## Resultats
