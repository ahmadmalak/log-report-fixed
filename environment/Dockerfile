# Pinned by digest for reproducibility. This digest must point at the same
# tag/architecture your Harbor provider will pull. Refresh it yourself with:
#   docker pull python:3.12-slim
#   docker inspect --format='{{index .RepoDigests 0}}' python:3.12-slim
# then paste the resulting sha256 below before running `harbor run`.
FROM python@sha256:c3d81d25b3154142b0b42eb1e61300024426268edeb5b5a26dd7ddf64d9daf28

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
