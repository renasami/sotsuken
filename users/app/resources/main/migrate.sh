(cd "${REPOSITORY_ROOT}/users")

echo `date '+%y/%m/%d %H:%M:%S'`
echo "一括SQLを実行します。"
psql -h 127.0.0.1 -p 9999 -U postgres -d sotsuken-users -f ./migrate.sql > ./result.log
echo `date '+%y/%m/%d %H:%M:%S'`
echo "一括SQLの実行が終了しました。"