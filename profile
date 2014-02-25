# jubatest environment for bash/zsh

export JUBATEST_HOME="$(cd $(dirname ${BASH_SOURCE:-${0}}); pwd)"
export PYTHONPATH="${JUBATEST_HOME}/lib:${PYTHONPATH}"
export PATH="${JUBATEST_HOME}/bin:${PATH}"
