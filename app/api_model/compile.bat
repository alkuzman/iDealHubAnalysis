protostub generate --proto ./protobuf/api_model.proto --mypy ./generated/api_model_pb2.pyi &
protoc -I=./protobuf --python_out=./generated ./protobuf/api_model.proto
