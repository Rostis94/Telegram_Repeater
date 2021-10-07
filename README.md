# Telethon setup
Installation:  
https://docs.telethon.dev/en/latest/basic/installation.html


Messages sending:  
https://docs.telethon.dev/en/latest/modules/client.html#telethon.client.messages.MessageMethods


# Run project
- Register app on https://my.telegram.org/auth
- Get `api_id` and `api_hash`
- Create file `Secrets.py` with following content:

```python
telegram_api_id = YOUR_API_ID
telegram_api_hash = "YOUR_API_HASH"
```

- Run `Dialogs.py` to get dialogs IDs
- Add to `Secrets.py` following lines:  

```python
source_channel_id = YOUR_SOURCE_CHANNEL_ID
destination_channel_id = YOUR_DESTINATION_CHANNEL_ID
```
- Run `Main.py` to start message listening
