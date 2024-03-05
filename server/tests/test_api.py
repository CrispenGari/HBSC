import httpx

url = "http://127.0.0.1:3001"


class TestAPI:
    def test_meta(self):
        q = """
        fragment MetaFragment on MetaResponse{
            programmer
            main
            description
            language
            libraries
        }
        query Meta{
            meta{
                ...MetaFragment
            }
        }
        """
        res = httpx.post(url, json={"query": q})
        assert res.json() == {
            "data": {
                "meta": {
                    "programmer": "@crispengari",
                    "main": "Heart Beat Sound Classification (HBSC)",
                    "description": "This is a graphql API for classifying heart beat sounds into 4 different categories from audios in real time. Given an audio of a heartbeat sound the API should be able to classify the sound's category with 100% confidence.",
                    "language": "python",
                    "libraries": ["pytorch", "torchaudio"],
                }
            }
        }
        assert res.status_code == 200
