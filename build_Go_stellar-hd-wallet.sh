#!/bin/bash
# Written for Fedora, dependent package names may differ...

echo " .:Run Pre-Build Tests:. "

rpm -q golang || needsdeps="true"

if [ $needsdeps ]; then
  echo "golang not installed, install that as root first!"
  exit 1
else echo "pre-build tests passed, starting build"
fi

if [ ! -d "~/bin" ]; then
  mkdir -p ~/bin
fi

if [ ! -d "~/go/src" ]; then
  mkdir -p ~/go/src
fi


export GOPATH=~/go
cd $GOPATH/src/
mkdir github.com
go get -v -u github.com/stellar/go
go get -v -u github.com/spf13/cobra
go get -v -u github.com/agl/ed25519
go get -v -u github.com/spf13/pflag
go get -v -u github.com/nullstyle/go-xdr
go get -v -u github.com/getsentry/raven-go
go get -v -u github.com/certifi/gocertifi
go get -v -u github.com/bartekn/go-bip39
go get -v -u github.com/pkg/errors
go get -v -u golang.org/x/crypto/pbkdf2
go build -o ~/bin/stellar-hd-wallet ~/go/src/github.com/stellar/go/tools/stellar-hd-wallet/main.go

chmod +x ~/bin/stellar-hd-wallet
