# cache the password for 15 minutes
git config --global credential.helper cache

echo "Enter a comment: "
read COMMENT
echo "--$COMMENT--"

git add .
git commit -m "$COMMENT"
git push
