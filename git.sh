git filter-branch --commit-filter '
        if [ "$GIT_COMMITTER_NAME" = "jokerdino" ];
        then
                GIT_COMMITTER_NAME="Barneedhar Vigneshwar";
        else
                git commit-tree "$@";
        fi' HEAD
