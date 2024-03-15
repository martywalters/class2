echo '*** Start ServerSocket in seperate command window'
#open seperate command window and run ServerSocktFileXfer.py 
echo '*** Remove old team_data.pkl file'
rm team_data.pkl
echo '*** run python code to Pickle It'
python3 -c 'from part3 import pickle_it;pickle_it()'
echo '*** run python code to move Pickle file to Client Folder'
python3 -c 'from part3 import move_pickle;move_pickle()'
echo '*** change to client directory'
cd client 
echo '*** run client socket to transfer file back to server '
python3 ClientSocketFileXfer.py 
echo '*** change back to main folder File transfer is finished'
cd ..
echo '*** unpickle the transfer file'
python3 -c 'from part3 import unpickle_it;unpickle_it()'

