# fisker_noob - projekt

Dette er et eksamensprojekt i Data Science Python. Projektet handler om at skulle identificere fiskearter via billedegenkendelse eller web-cam. 
Projektet er dog desværre ikke kommet helt i mål.

Projektet bruger følgende teknologier:
absl-py==1.0.0
astunparse==1.6.3
cachetools==5.1.0
certifi==2022.5.18.1
charset-normalizer==2.0.12
flatbuffers==1.12
gast==0.4.0
google-auth==2.6.6
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.46.3
h5py==3.6.0
idna==3.3
importlib-metadata==4.11.4
keras==2.9.0
Keras-Preprocessing==1.1.2
libclang==14.0.1
Markdown==3.3.7
numpy==1.22.4
oauthlib==3.2.0
opt-einsum==3.3.0
packaging==21.3
protobuf==3.20.1
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==3.0.9
requests==2.27.1
requests-oauthlib==1.3.1
rsa==4.8
six==1.16.0
tensorboard==2.9.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.9.0
tensorflow-estimator==2.9.0
tensorflow-gpu==2.9.0
tensorflow-io==0.26.0
tensorflow-io-gcs-filesystem==0.26.0
tensorflow-io-plugin-gs-nightly==0.18.0.dev20210513213318
termcolor==1.1.0
typing_extensions==4.2.0
urllib3==1.26.9
Werkzeug==2.1.2
wrapt==1.14.1
zipp==3.8.0

Der er brugt anaconda til at få projektet til at køre lokalt.
Hertil projektet er der også brugt Tensorflow model API: https://github.com/tensorflow/models

Man kan hente projektet ned og køre de enkelte celler i detection.pynb - dog mangler trænning og tests billederne (da de ikke må lægges op af mig) og andre filer - 
fordi de er for store til github. Har dog prøvet at lave en alternativ løsning i til de større filer i detection.pynb, men man mangler stadigvæk billederne.

Status:
- Billederne til trænning af neural network er hentet ned 
- Der er blevet lavet en modifier så billederne kan skaleres ned
- I mangel på billeder er der en "random billedgenerator"
- Maksinen er blevet konstrueret men der er en path som driller et eller andet sted så man ikke kan kører maskinen igennem nye billeder
- Mangler at hente opskrifter
- Mangler at webscrabe diverse handlemuligheder 
- Mangler at sammenligne priser

Der har været meget bøvl med stierne i projektet og det tilhørende tensorflow API, som hele tiden skulle rettes frem og tilbage. 
Har lavet et workaround men før tog det meget tid, og der er stadigvæk fejl i projektet som kan skyldes måske workarounded. 
Webcam har været svært at oprette forbindelse til i det virtuelle miljø, så der er gået for meget tid med det og derfor kører det lokalt.
Det har også taget meget længe at træne maskinen ad gangen - op til flere timer. Skulle nok at brugt en optimizer, såsom Adam, til beregne steps mm.
