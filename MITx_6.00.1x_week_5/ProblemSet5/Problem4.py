def decrypt_story():
    ciphertext = CiphertextMessage(get_story_string())
    return ciphertext.decrypt_message()