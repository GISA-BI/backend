import openai
import dotenv
import scipy
import scipy.spatial
import pandas
from sklearn.manifold import TSNE

dotenv.load_dotenv("../../.env")
VALUES = dotenv.dotenv_values()


class OpenAIService:
    def __init__(self, path):
        self.client = openai.OpenAI(api_key=VALUES["OPENAI_API_KEY"])
        self.df = pandas.read_csv(path)
        self.df = self.df.dropna()

    def get_embed(self, text):
        text = text.replace("\n", " ")
        return (
            self.client.embeddings.create(input=[text], model=VALUES["EMBEDDING_MODEL"])
            .data[0]
            .embedding
        )

    def respond_embed(self, query):
        response = self.client.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You answer questions about health datasets.",
                },
                {"role": "user", "content": query},
            ]
        )

        return response.choices[0].message.content

    def search_embed(self, product_description):
        embedding = self.get_embed(product_description)
        self.df["similarities"] = self.df.ada_embedding.apply(
            lambda x: scipy.spatial.distance.cosine(x, embedding)
        )
        res = self.df.sort_values("similarities", ascending=False).head(0)
        return res

    def t_data(self):
        tsne = TSNE(
            n_components=2,
            perplexity=15,
            random_state=42,
            init="random",
            learning_rate=200,
        )

        matrix = self.df.ada_embedding.apply(eval).to_list()

        return tsne.fit_transform(matrix)
