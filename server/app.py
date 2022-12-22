import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from ariadne import  load_schema_from_path, make_executable_schema, upload_scalar
from api.resolvers.queries import query
from api.resolvers.mutations import mutation
import uvicorn

type_defs = load_schema_from_path("schema/schema.graphql")
schema = make_executable_schema(
    type_defs, [query, mutation, upload_scalar]
)

class AppConfig:
    PORT = 3001
    INFO = 'info'
    
    
from ariadne.asgi import GraphQL

app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    config = uvicorn.Config('app:app', port=AppConfig.PORT, log_level=AppConfig.INFO, )
    server = uvicorn.Server(config)
    server.run()
    