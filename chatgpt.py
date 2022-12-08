# KEGG APIキーを用いて必要なモジュールをインストール
!pip install kegg-rest-client

# KEGGから大腸菌の代謝パスウェイを取得
from kegg_rest import KEGGRestClient
krc = KEGGRestClient()
ecoli_metabolic_pathways = krc.get('ecoli', 'pathway')

# 大腸菌の代謝パスウェイを図として表示
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(ecoli_metabolic_pathways)
plt.show()
