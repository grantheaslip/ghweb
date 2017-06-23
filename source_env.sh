# Via https://unix.stackexchange.com/a/79077
# Run "source ./source_env.sh" or add it to ~/.venvs/postactivate

set -o allexport
source ./.env
set +o allexport
