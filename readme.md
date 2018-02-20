This is a place to put general comments.

Always update conda before installing packages.
conda update conda
conda update --all

When installing packages:
Try Conda first.
Then try PIP.
Then you have to use source. To insall then you will navigate to the directory and do "python setup.py install" from command prompt.

Useful Git commands:
git clone https://github.com/treujc/Notebook.git
git status
git add
git commit -m 'Add comments here.'
git push
git pull
git config --global user.name 'treujc'                                  
git config --global user.email 'evan.trevathan@bp.com'                              
git config --global core.editor atom
git remote -v
git checkout master
git pull https://github.com/gSchool/ds-week-0.git master
Resolve any merge conflicts
git commit -a -m 'merged from upstream'
git push origin master
git checkout --theirs /path/to/file                                                                        
git checkout --ours /path/to/file                                                  
git log filename #this will allow you to git checkout hash to revert to a point in time.   
Then you need to add it and commit       
git add /path/to/file                                                              
git commit -m 'fixed merge'                                                        
git push
Note: When you want to make changes to a GitHub repository you will need to fork it. To view the always current version of the repository clone it.

Some useful bash commands:
rmdir  "removes a directory.""
rm -rf "removes a directory and all its contents."

Remember the D.R.Y. principal. Don't Repeat Yourself!
