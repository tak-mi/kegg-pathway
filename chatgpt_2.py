# KEGG APIキーを用いて必要なモジュールをインストール
!pip install kegg-rest-client

# KEGGから大腸菌の代謝経路を取得
from kegg_rest import KEGGRestClient
krc = KEGGRestClient()
ecoli_metabolic_pathways = krc.get('ecoli', 'pathway')

# グルコースからフェニルアラニンまでの代謝経路を抽出
glucose_to_phenylalanine_pathway = {}
for entry in ecoli_metabolic_pathways:
    if 'glucose' in entry and 'phenylalanine' in entry:
        glucose_to_phenylalanine_pathway = entry

# グルコースからフェニルアラニンまでの代謝経路と酵素を図として表示
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(glucose_to_phenylalanine_pathway)
