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
    --workdir /workspace/go-jsonnet \ # cloned ahead of time
    dan-buildbox:$(git rev-parse --short HEAD) \
    llm prompt \
        --tool bazelisk \
        --tools-debug \
        --chain-limit 0 \
        --model openrouter/openai/gpt-5-codex \
        "Can you list the Bazel test targets under this repo?"
```
