# buildbox

Building the container:
```
container build --tag dan-buildbox:$(git rev-parse --short HEAD) .
```

Running `llm` inside the container:
```
container run \
    --interactive \
    --tty \
    --rm \
    --env OPENROUTER_API_KEY="$OPENROUTER_API_KEY" \
    --env OPENROUTER_KEY="$OPENROUTER_KEY" \
    --volume="$(pwd)/workspace":/workspace \
    --volume="$(pwd)/workspace/aider":/root/.aider \
    --workdir /workspace/go-jsonnet  \
    dan-buildbox:$(git rev-parse --short HEAD) \
    llm prompt \
        --tool aider \
        --tool bash \
        --tool bazelisk \
        --tools-debug \
        --chain-limit 0 \
        --model openrouter/openai/gpt-5-codex \
        "Can you see any missing unit tests in this repo (go-jsonnet)?"
```
