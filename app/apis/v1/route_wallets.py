from fastapi import APIRouter, Depends, HTTPException, status
from utils.bitcoin import (
    generate_mnemonic,
    get_master_privatekey,
    get_xpub_from_private_key,
)

router = APIRouter()


@router.get("/generate")
def new_mnemonic():
    # dummy endpoint
    words = generate_mnemonic()
    key = get_master_privatekey(words)
    xpub = get_xpub_from_private_key(key)
    return {"mnemonic": words, "private_key": key, "xpub": xpub}
