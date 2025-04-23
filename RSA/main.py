from RSA import RSA



bob = RSA(p=17, q=23)

print("bob public key: " + str(bob.get_public_key()))
print("bob private key: " + str(bob.get_private_key()))

alice = RSA(p=19, q=29)

print("alice public key: " + str(alice.get_public_key()))
print("alice private key: " + str(alice.get_private_key()))

message_from_bob_to_alice = "Hi Alice!"

encrypted_message_to_alice = alice.encrypt(message_from_bob_to_alice, public_key=alice.get_public_key())
print("\nencrypted message sent to alice:", encrypted_message_to_alice)

decrypted_message_from_bob = alice.decrypt(encrypted_message_to_alice)
print("Decrypted Message by Alice:", decrypted_message_from_bob)

message_from_alice_to_bob = "Hello Bob!"

encrypted_message_to_bob = bob.encrypt(message_from_alice_to_bob, public_key=bob.get_public_key())
print("\nEncrypted Message Sent to Bob:", encrypted_message_to_bob)

decrypted_message_from_alice = bob.decrypt(encrypted_message_to_bob)
print("Decrypted Message by Bob:", decrypted_message_from_alice)

print("\n---------------------------------------\n")

message_from_alice = "Hello Bob!"
signature = alice.encrypt(message_from_alice, public_key=alice.get_private_key())

decrypted_message = message_from_alice

print("--- Bob Verifying Alice's Signature ---")
decrypted_signature = alice.decrypt(signature, private_key=alice.get_public_key())
print("Decrypted Signature:", decrypted_signature)

if decrypted_signature == decrypted_message:
    print("Signature Verified: Message is authentic!")
else:
    print("Signature Verification Failed: Message may be forged or altered!")

