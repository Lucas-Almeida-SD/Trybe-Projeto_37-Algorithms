from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    word = "AABBCC"

    assert encrypt_message(word, len(word)) == "CCBBAA"

    assert encrypt_message(word, 0) == "CCBBAA"

    assert encrypt_message(word, -1) == "CCBBAA"

    assert encrypt_message(word, 3) == "BAA_CCB"

    assert encrypt_message(word, 4) == "CC_BBAA"

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(word, "1")
