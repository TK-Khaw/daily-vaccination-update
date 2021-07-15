#!/usr/bin/sh

cd $CITF_DIR
git fetch

if [[ $(git rev-parse HEAD) != $(git rev-parse origin/HEAD) ]]
then
	echo 'Need pull!!!'
	git pull
	MSG=$(git log -1 --pretty="format:$COMMIT_FORMAT")
	cd $JKJAV_AUTO_DIR

	while read rgx
	do
		BUF=$(echo $MSG | grep -E "^$rgx$" )
		if [[ $BUF != '' ]]; then break; fi
	done < wl_msg_ptn

	if [[ $BUF != '' ]]
	then
		$PYTHON3 $AUTONOT_SCRIPT "$MSG"
	else
		echo 'Not related'
	fi
else
	echo 'Update to date!'
fi
