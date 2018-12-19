# Using scp

The basic syntax of scp is very simple to memorize. It looks like this

### > scp source_file_path destination_file_path
Depending on the host, the file path should include the full host address, port number, username and password along with the directory path.

So if you are "sending" file from your local machine to a remote machine (uploading) the syntax would look like this

### > scp ~/my_local_file.txt user@remote_host.com:/some/remote/directory
When copying file from remote host to local host (downloading), its looks just the reverse

### scp user@remote_host.com:/some/remote/directory ~/my_local_file.txt

### <i>just download the file </i>
### scp user@192.168.1.3:/some/path/file.txt .