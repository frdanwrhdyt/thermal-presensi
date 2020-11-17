
 

import base64, codecs
magic = 'IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KIyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIG51bXB5IGltcG9ydCBzYXZlCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKaW1wb3J0IHJlLHV1aWQKaW1wb3J0IHRpbWUKaW1wb3J0IGN2MgppbXBvcnQgc3lzCmltcG9ydCBkYXRldGltZQppbXBvcnQgbnVtcHkgYXMgbnAKCiNmcm9tIG11bHRpcHJvY2Vzc2luZyBpbXBvcnQgUHJvY2VzcywgUGlwZQojaW1wb3J0IGltdXRpbHMKCmZyb20gZmxhc2sgaW1wb3J0IEZsYXNrLCByZW5kZXJfdGVtcGxhdGUsIFJlc3BvbnNlCmltcG9ydCB0aHJlYWRpbmcKaW1wb3J0IGFyZ3BhcnNlCgpmcm9tIHNldHRpbmdzIGltcG9ydCAqCgp0cnk6CiAgZnJvbSBxdWV1ZSBpbXBvcnQgUXVldWUKZXhjZXB0IEltcG9ydEVycm9yOgogIGZyb20gUXVldWUgaW1wb3J0IFF1ZXVlCmltcG9ydCBwbGF0Zm9ybQoKYXBwID0gRmxhc2soX19uYW1lX18pCkJVRl9TSVpFID0gMgpxID0gUXVldWUoQlVGX1NJWkUpCnJlZCA9ICgwLDAsMjU1KQpncmVlbiA9ICgwLDI1NSwwKQoKY29sb3JNYXBUeXBlID0gMAphZGRyZXNzaXAgPSAnMTkyLjE2OC44LjEwMycKYWRkcmVzc3BvcnQgPSA4MDAwCmxpbWl0VCA9IDM3LjMKYWRkcmVmID0gMApzaGFwZSA9MgphZGQxID0gImRjOmE2OjMyOjZmOmJjOjM0IgphZGQyID0gImRjOmE2OjMyOjZmOmJjOjMzIgpzaW1wYW4gPSAwCgpvdXRwdXRGcmFtZSA9IE5vbmUKbG9jayA9IHRocmVhZGluZy5Mb2NrKCkKCgpkZWYgcHlfZnJhbWVfY2FsbGJhY2soZnJhbWUsIHVzZXJwdHIpOgoKICBhcnJheV9wb2ludGVyID0gY2FzdChmcmFtZS5jb250ZW50cy5kYXRhLCBQT0lOVEVSKGNfdWludDE2ICogKGZyYW1lLmNvbnRlbnRzLndpZHRoICogZnJhbWUuY29udGVudHMuaGVpZ2h0KSkpCiAgZGF0YSA9IG5wLmZyb21idWZmZXIoYXJyYXlfcG9pbnRlci5jb250ZW50cywgZHR5cGU9bnAuZHR5cGUobnAudWludDE2KSkucmVzaGFwZShmcmFtZS5jb250ZW50cy5oZWlnaHQsIGZyYW1lLmNvbnRlbnRzLndpZHRoKSAjIG5vIGNvcHkKCiAgIyBkYXRhID0gbnAuZnJvbWl0ZXIoCiAgIyAgIGZyYW1lLmNvbnRlbnRzLmRhdGEsIGR0eXBlPW5wLmR0eXBlKG5wLnVpbnQ4KSwgY291bnQ9ZnJhbWUuY29udGVudHMuZGF0YV9ieXRlcwogICMgKS5yZXNoYXBlKAogICMgICBmcmFtZS5jb250ZW50cy5oZWlnaHQsIGZyYW1lLmNvbnRlbnRzLndpZHRoLCAyCiAgIyApICMgY29weQoKICBpZiBmcmFtZS5jb250ZW50cy5kYXRhX2J5dGVzICE9ICgyICogZnJhbWUuY29udGVudHMud2lkdGggKiBmcmFtZS5jb250ZW50cy5oZWlnaHQpOgogICAgcmV0dXJuCgogIGlmIG5vdCBxLmZ1bGwoKToKICAgIHEucHV0KGRhdGEpCgpQVFJfUFlfRlJBTUVfQ0FMTEJBQ0sgPSBDRlVOQ1RZUEUoTm9uZSwgUE9JTlRFUih1dmNfZnJhbWUpLCBjX3ZvaWRfcCkocHlfZnJhbWVfY2FsbGJhY2spCgoKQGFwcC5yb3V0ZSgnLycpCmRlZiBpbmRleCgpOgogICAgIiIiVmlkZW8gc3RyZWFtaW5nIGhvbWUgcGFnZS4iIiIKICAgIHJldHVybiByZW5kZXJfdGVtcGxhdGUoJ2luZGV4Lmh0bWwnKQoKZGVmIGdlbigpOgogICAgIiIiVmlkZW8gc3RyZWFtaW5nIGdlbmVyYXRvciBmdW5jdGlvbi4iIiIKICAgIGdsb2JhbCBhZGRyZWYsIHNpbXBhbgogICAgZ2xvYmFsIG91dHB1dEZyYW1lLCBsb2NrCgogICAgaW1hZ2VfcGF0aCA9IHInXHRlbXBsYXRlXGdlZWtzLmpwZycKICAgIGN0eCA9IFBPSU5URVIodXZjX2NvbnRleHQpKCkKICAgIGRldiA9IFBPSU5URVIodXZjX2RldmljZSkoKQogICAgZGV2aCA9IFBPSU5URVIodXZjX2RldmljZV9oYW5kbGUpKCkKICAgIGN0cmwgPSB1dmNfc3RyZWFtX2N0cmwoKQogICAgcmVzID0gbGlidXZjLnV2Y19pbml0KGJ5cmVmKGN0eCksIDApCiAgICBpZiByZXMgPCAwOgogICAgICAgIHByaW50KCJ1dmNfaW5pdCBlcnJvciIpCiAgICAgICAgZXhpdCgxKQogICAgdHJ5OgogICAgICAgIG1hZD0gKCc6Jy5qb2luKHJlLmZpbmRhbGwoJy4uJywgJyUwMTJ4JyAlIHV1aWQuZ2V0bm9kZSgpKSkpCiAgICAgICAgaWYgKG1hZCAhPSBhZGQxKSBhbmQgKG1hZCAhPSBhZGQyKToKICAgICAgICAgICAgcHJpbnQoImVycm9yIDAxOiB1dmNfZmluZF9kZXZpY2UgZXJyb3IiKQogICAgICAgICAgICBleGl0KDEpCiAgICAgICAgcmVzID0gbGlidXZjLnV2Y19maW5kX2RldmljZShjdHgsIGJ5cmVmKGRldiksIFBUX1VTQl9WSUQsIFBUX1VTQl9QSUQsIDApCiAgICAgICAgaWYgcmVzIDwgMDoKICAgICAgICAgICAgcHJpbnQoImVycm9yIDAyOiB1dmNfZmluZF9kZXZpY2UgZXJyb3IiKQogICAgICAgICAgICBleGl0KDEpCiAgICAgICAgdHJ5OgogICAgICAgICAgICAKICAgICAgICAgICAgcmVzID0gbGlidXZjLnV2Y19vcGVuKGRldiwgYnlyZWYoZGV2aCkpCiAgICAgICAgICAgIGlmIHJlcyA8IDA6CiAgICAgICAgICAgICAgICBwcmludCgiZXJyb3IgMDM6IHV2Y19vcGVuIGVycm9yIikKICAgICAgICAgICAgICAgIGV4aXQoMSkKICAgICAgICAgICAgcHJpbnQoImRldmljZSBvcGVuZWQhIikKICAgICAgICAgICAgI3ByaW50KCJUaGUgTUFDIGFkZHJlc3MgaW4gZm9ybWF0dGVkIGFuZCBsZXNzIGNvbXBsZXggd2F5IGlzIDogIikgCiAgICAgICAgICAgICNwcmludCgnOicuam9pbihyZS5maW5kYWxsKCcuLicsICclMDEyeCcgJSB1dWlkLmdldG5vZGUoKSkpKQogICAgICAgICAgICBwcmludF9kZXZpY2VfaW5mbyhkZXZoKQogICAgICAgICAgICBwcmludF9kZXZpY2VfZm9ybWF0cyhkZXZoKQogICAgICAgICAgICBmcmFtZV9mb3JtYXRzID0gdXZjX2dldF9mcmFtZV9mb3JtYXRzX2J5X2d1aWQoZGV2aCwgVlNfRk1UX0dVSURfWTE2KQogICAgICAgICAgICBpZiBsZW4oZnJhbWVfZm9ybWF0cykgPT0gMDoKICAgICAgICAgICAgICAgIHByaW50KCJlcnJvciAwNDogZGV2aWNlIGRvZXMgbm90IHN1cHBvcnQgWTE2IikKICAgICAgICAgICAgICAgIGV4aXQoMSkKICAgICAgICAgICAgbGlidXZjLnV2Y19nZXRfc3RyZWFtX2N0cmxfZm9ybWF0X3NpemUoZGV2aCwgYnlyZWYoY3RybCksIFVWQ19GUkFNRV9GT1JNQVRfWTE2LGZyYW1lX2Zvcm1hdHNbMF0ud1dpZHRoLCBmcmFtZV9mb3JtYXRzWzBdLndIZWlnaHQsIGludCgxZTcgLyBmcmFtZV9mb3JtYXRzWzBdLmR3RGVmYXVsdEZyYW1lSW50ZXJ2YWwpKQogICAgICAgICAgICByZXMgPSBsaWJ1dmMudXZjX3N0YXJ0X3N0cmVhbWluZyhkZXZoLCBieXJlZihjdHJsKSwgUFRSX1BZX0ZSQU1FX0NBTExCQUNLLCBOb25lLCAwKQogICAgICAgICAgICBpZiByZXMgPCAwOgogICAgICAgICAgICAgICAgcHJpbnQoImVycm9yIDA1OiB1dmNfc3RhcnRfc3RyZWFtaW5nIGZhaWxlZDogezB9Ii5mb3JtYXQocmVzKSkKICAgICAgICAgICAgICAgIGV4aXQoMSkKICAgICAgICAgICAgCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgICAgICAgICAgZGF0YSA9IHEuZ2V0KFRydWUsIDUwMCkKICAgICAgICAgICAgICAgICAgICBpZiBkYXRhIGlzIE5vbmU6CiAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgICAgICAgICAgZGF0YSA9IGN2Mi5yZXNpemUoZGF0YVs6LDpdLCAoNjQwLCA0ODApKQogICAgICAgICAgICAgICAgICAgIG1heFZhbCA9IGRhdGFbMzIwLDI0MF0gCiAgICAgICAgICAgICAgICAgICAgI2ltZyA9IHJhd190b184Yml0KGRhdGEpCiAgICAgICAgICAgICAgICAgICAgaW1nID0gY3YyLkxVVChyYXdfdG9fOGJpdChkYXRhKSwgZ2VuZXJhdGVfY29sb3VyX21hcCgpKQogICAgICAgICAgICAgICAgICAgIGNscjEgPSBncmVlbgogICAgICAgICAgICAgICAgICAgIHZhbDEgPSBrdG9jKG1heFZhbCkKICAgICAgICAgICAgICAgICAgICB2YWwxID0gdmFsMSArIGFkZHJlZgogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIGlmICh2YWwxID4gbGltaXRUKToKICAgICAgICAgICAgICAgICAgICAgICAgY2xyMSA9IHJlZAogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIGlmIHNoYXBlID09IDA6CiAgICAgICAgICAgICAgICAgICAgICAgIHBsdXMoaW1nLGNscjEpCiAgICAgICAgICAgICAgICAgICAgICAgIHBvcyA9ICgzMTEsOTUpCiAgICAgICAgICAgICAgICAgICAgZWxpZiBzaGFwZSA9PSAxOgogICAgICAgICAgICAgICAgICAgICAgICB0cmlhbmdsZShpbWcsY2xyMSkKICAgICAgICAgICAgICAgICAgICAgICAgcG9zID0gKDMxMSwxMjApCiAgICAgICAgICAgICAgICAgICAgZWxpZiBzaGFwZSA9PSAyOgogICAgICAgICAgICAgICAgICAgICAgICBzcXVhcmUoaW1nLGNscjEpIAogICAgICAgICAgICAgICAgICAgICAgICBwb3MgPSAoMzExLDk1KQogICAgICAgICAgICAgICAgICAgIGRpc3BsYXlfdGVtcGVyYXR1cmUoaW1nLCBtYXhWYWwsIHBvcyAsIGNscjEpCiAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgaWYgKHZhbDEgPiBsaW1pdFQpOiAKICAgICAgICAgICAgICAgICAgICAgICAgZmlsZW5hbWUgPSAnc2F2ZWRJbWFnZS5qcGcnCiAgICAgICAgICAgICAgICAgICAgICAgIGR0ID0gc3RyKGRhdGV0aW1lLmRhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCIlWS0lbS0lZCAlSDolTTolUyIpKSAKICAgICAgICAgICAgICAgICAgICAgICAgZnJhbWVkYXRlID0gaW1nLmNvcHkoKQogICAgICAgICAgICAgICAgICAgICAgICBmcmFtZWRhdGUgPSBjdjIucHV0VGV4dChmcmFtZWRhdGUsIGR0LCAoMTAsIDQ2MCksIGN2Mi5GT05UX0hFUlNIRVlfU0lNUExFWCwgMC43LCAoMjU1LDI1NSwyNTUpLDIgKSAKICAgICAgICAgICAgICAgICAgICAgICAgY3YyLmltd3JpdGUoJ3N0YXRpYy8nKyBmaWxlbmFtZSwgZnJhbWVkYXRlKQogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIGlmICh2YWwxID4gbGltaXRUKSBhbmQgKHNpbXBhbiA9PTApOgogICAgICAgICAgICAgICAgICAgICAgICBjbHIxID0gcmVkCiAgICAgICAgICAgICAgICAgICAgICAgIHNpbXBhbiA9IDEKICAgICAgICAgICAgICAgICAgICAgICAgc2F2ZSgnc2lnbi5ucHknLCBzaW1wYW4pCiAgICAgICAgICAgICAgICAgICAgZWxpZiAodmFsMSA8PSBsaW1pdFQpIGFuZCAoc2ltcGFuID09MSk6CiAgICAgICAgICAgICAgICAgICAgICAgIHNpbXBhbiA9IDAKICAgICAgICAgICAgICAgICAgICAgICAgc2F2ZSgnc2lnbi5ucHknLCBzaW1wYW4pCiAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgI2ZyYW1lMSA9IGltdXRpbHMucmVzaXplKGltZyw2NDAsNDgwKQogICAgICAgICAgICAgICAgICAgIHdpdGggbG9jazoKICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0RnJhbWUgPSBpbWcuY29weSgpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICNmcmFtZSA9IGN2Mi5pbWVuY29kZSgnLmpwZycsIGltZylbMV0udG9ieXRlcygpCiAgICAgICAgICAgICAgICAgICAgI3lpZWxkIChiJy0tZnJhbWVcclxuJ2InQ29udGVudC1UeXBlOiBpbWFnZS9qcGVnXHJcblxyXG4nICsgZnJhbWUgKyBiJ1xyXG4nKQogICAgICAgICAgICAgICAgICAgIGN2M'
love = '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'
god = 'A0OCwgNDgsIDQ4LCA0OSwgNDksIDQ5LCA1MCwgNTAsIDUwLCA1MSwgNTEsIDUxLCA1MiwgNTIsIDUyLCA1MywgNTMsIDUzLCA1NCwgNTQsIDU0LCA1NSwgNTUsIDU1LCA1NiwgNTYsIDU2LCA1NywgNTcsIDU3LCA1OCwgNTgsIDU4LCA1OSwgNTksIDU5LCA2MCwgNjAsIDYwLCA2MSwgNjEsIDYxLCA2MiwgNjIsIDYyLCA2MywgNjMsIDYzLCA2NCwgNjQsIDY0LCA2NSwgNjUsIDY1LCA2NiwgNjYsIDY2LCA2NywgNjcsIDY3LCA2OCwgNjgsIDY4LCA2OSwgNjksIDY5LCA3MCwgNzAsIDcwLCA3MSwgNzEsIDcxLCA3MiwgNzIsIDcyLCA3MywgNzMsIDczLCA3NCwgNzQsIDc0LCA3NSwgNzUsIDc1LCA3NiwgNzYsIDc2LCA3NywgNzcsIDc3LCA3OCwgNzgsIDc4LCA3OSwgNzksIDc5LCA4MCwgODAsIDgwLCA4MSwgODEsIDgxLCA4MiwgODIsIDgyLCA4MywgODMsIDgzLCA4NCwgODQsIDg0LCA4NSwgODUsIDg1LCA4NiwgODYsIDg2LCA4NywgODcsIDg3LCA4OCwgODgsIDg4LCA4OSwgODksIDg5LCA5MCwgOTAsIDkwLCA5MSwgOTEsIDkxLCA5MiwgOTIsIDkyLCA5MywgOTMsIDkzLCA5NCwgOTQsIDk0LCA5NSwgOTUsIDk1LCA5NiwgOTYsIDk2LCA5NywgOTcsIDk3LCA5OCwgOTgsIDk4LCA5OSwgOTksIDk5LCAxMDAsIDEwMCwgMTAwLCAxMDEsIDEwMSwgMTAxLCAxMDIsIDEwMiwgMTAyLCAxMDMsIDEwMywgMTAzLCAxMDQsIDEwNCwgMTA0LCAxMDUsIDEwNSwgMTA1LCAxMDYsIDEwNiwgMTA2LCAxMDcsIDEwNywgMTA3LCAxMDgsIDEwOCwgMTA4LCAxMDksIDEwOSwgMTA5LCAxMTAsIDExMCwgMTEwLCAxMTEsIDExMSwgMTExLCAxMTIsIDExMiwgMTEyLCAxMTMsIDExMywgMTEzLCAxMTQsIDExNCwgMTE0LCAxMTUsIDExNSwgMTE1LCAxMTYsIDExNiwgMTE2LCAxMTcsIDExNywgMTE3LCAxMTgsIDExOCwgMTE4LCAxMTksIDExOSwgMTE5LCAxMjAsIDEyMCwgMTIwLCAxMjEsIDEyMSwgMTIxLCAxMjIsIDEyMiwgMTIyLCAxMjMsIDEyMywgMTIzLCAxMjQsIDEyNCwgMTI0LCAxMjUsIDEyNSwgMTI1LCAxMjYsIDEyNiwgMTI2LCAxMjcsIDEyNywgMTI3LCAxMjgsIDEyOCwgMTI4LCAxMjksIDEyOSwgMTI5LCAxMzAsIDEzMCwgMTMwLCAxMzEsIDEzMSwgMTMxLCAxMzIsIDEzMiwgMTMyLCAxMzMsIDEzMywgMTMzLCAxMzQsIDEzNCwgMTM0LCAxMzUsIDEzNSwgMTM1LCAxMzYsIDEzNiwgMTM2LCAxMzcsIDEzNywgMTM3LCAxMzgsIDEzOCwgMTM4LCAxMzksIDEzOSwgMTM5LCAxNDAsIDE0MCwgMTQwLCAxNDEsIDE0MSwgMTQxLCAxNDIsIDE0MiwgMTQyLCAxNDMsIDE0MywgMTQzLCAxNDQsIDE0NCwgMTQ0LCAxNDUsIDE0NSwgMTQ1LCAxNDYsIDE0NiwgMTQ2LCAxNDcsIDE0NywgMTQ3LCAxNDgsIDE0OCwgMTQ4LCAxNDksIDE0OSwgMTQ5LCAxNTAsIDE1MCwgMTUwLCAxNTEsIDE1MSwgMTUxLCAxNTIsIDE1MiwgMTUyLCAxNTMsIDE1MywgMTUzLCAxNTQsIDE1NCwgMTU0LCAxNTUsIDE1NSwgMTU1LCAxNTYsIDE1NiwgMTU2LCAxNTcsIDE1NywgMTU3LCAxNTgsIDE1OCwgMTU4LCAxNTksIDE1OSwgMTU5LCAxNjAsIDE2MCwgMTYwLCAxNjEsIDE2MSwgMTYxLCAxNjIsIDE2MiwgMTYyLCAxNjMsIDE2MywgMTYzLCAxNjQsIDE2NCwgMTY0LCAxNjUsIDE2NSwgMTY1LCAxNjYsIDE2NiwgMTY2LCAxNjcsIDE2NywgMTY3LCAxNjgsIDE2OCwgMTY4LCAxNjksIDE2OSwgMTY5LCAxNzAsIDE3MCwgMTcwLCAxNzEsIDE3MSwgMTcxLCAxNzIsIDE3MiwgMTcyLCAxNzMsIDE3MywgMTczLCAxNzQsIDE3NCwgMTc0LCAxNzUsIDE3NSwgMTc1LCAxNzYsIDE3NiwgMTc2LCAxNzcsIDE3NywgMTc3LCAxNzgsIDE3OCwgMTc4LCAxNzksIDE3OSwgMTc5LCAxODAsIDE4MCwgMTgwLCAxODEsIDE4MSwgMTgxLCAxODIsIDE4MiwgMTgyLCAxODMsIDE4MywgMTgzLCAxODQsIDE4NCwgMTg0LCAxODUsIDE4NSwgMTg1LCAxODYsIDE4NiwgMTg2LCAxODcsIDE4NywgMTg3LCAxODgsIDE4OCwgMTg4LCAxODksIDE4OSwgMTg5LCAxOTAsIDE5MCwgMTkwLCAxOTEsIDE5MSwgMTkxLCAxOTIsIDE5MiwgMTkyLCAxOTMsIDE5MywgMTkzLCAxOTQsIDE5NCwgMTk0LCAxOTUsIDE5NSwgMTk1LCAxOTYsIDE5NiwgMTk2LCAxOTcsIDE5NywgMTk3LCAxOTgsIDE5OCwgMTk4LCAxOTksIDE5OSwgMTk5LCAyMDAsIDIwMCwgMjAwLCAyMDEsIDIwMSwgMjAxLCAyMDIsIDIwMiwgMjAyLCAyMDMsIDIwMywgMjAzLCAyMDQsIDIwNCwgMjA0LCAyMDUsIDIwNSwgMjA1LCAyMDYsIDIwNiwgMjA2LCAyMDcsIDIwNywgMjA3LCAyMDgsIDIwOCwgMjA4LCAyMDksIDIwOSwgMjA5LCAyMTAsIDIxMCwgMjEwLCAyMTEsIDIxMSwgMjExLCAyMTIsIDIxMiwgMjEyLCAyMTMsIDIxMywgMjEzLCAyMTQsIDIxNCwgMjE0LCAyMTUsIDIxNSwgMjE1LCAyMTYsIDIxNiwgMjE2LCAyMTcsIDIxNywgMjE3LCAyMTgsIDIxOCwgMjE4LCAyMTksIDIxOSwgMjE5LCAyMjAsIDIyMCwgMjIwLCAyMjEsIDIyMSwgMjIxLCAyMjIsIDIyMiwgMjIyLCAyMjMsIDIyMywgMjIzLCAyMjQsIDIyNCwgMjI0LCAyMjUsIDIyNSwgMjI1LCAyMjYsIDIyNiwgMjI2LCAyMjcsIDIyNywgMjI3LCAyMjgsIDIyOCwgMjI4LCAyMjksIDIyOSwgMjI5LCAyMzAsIDIzMCwgMjMwLCAyMzEsIDIzMSwgMjMxLCAyMzIsIDIzMiwgMjMyLCAyMzMsIDIzMywgMjMzLCAyMzQsIDIzNCwgMjM0LCAyMzUsIDIzNSwgMjM1LCAyMzYsIDIzNiwgMjM2LCAyMzcsIDIzNywgMjM3LCAyMzgsIDIzOCwgMjM4LCAyMzksIDIzOSwgMjM5LCAyNDAsIDI0MCwgMjQwLCAyNDEsIDI0MSwgMjQxLCAyNDIsIDI0MiwgMjQyLCAyNDMsIDI0MywgMjQzLCAyNDQsIDI0NCwgMjQ0LCAyNDUsIDI0NSwgMjQ1LCAyNDYsIDI0NiwgMjQ2LCAyNDcsIDI0NywgMjQ3LCAyNDgsIDI0OCwgMjQ4LCAyNDksIDI0OSwgMjQ5LCAyNTAsIDI1MCwgMjUwLCAyNTEsIDI1MSwgMjUxLCAyNTIsIDI1MiwgMjUyLCAyNTMsIDI1MywgMjUzLCAyNTQsIDI1NCwgMjU0LCAyNTUsIDI1NSwgMjU1XTsKICAgIGNvbG9ybWFwX3JhaW5ib3cgPSBbMSwgMywgNzQsIDAsIDMsIDc0LCAwLCAzLCA3NSwgMCwgMywgNzUsIDAsIDMsIDc2LCAwLCAzLCA3NiwgMCwgMywgNzcsIDAsIDMsIDc5LCAwLCAzLCA4MiwgMCwgNSwgODUsIDAsIDcsIDg4LCAwLCAxMCwgOTEsIDAsIDE0LCA5NCwgMCwgMTksIDk4LCAwLCAyMiwgMTAwLCAwLCAyNSwgMTAzLCAwLCAyOCwgMTA2LCAwLCAzMiwgMTA5LCAwLCAzNSwgMTEyLCAwLCAzOCwgMTE2LCAwLCA0MCwgMTE5LCAwLCA0MiwgMTIzLCAwLCA0NSwgMTI4LCAwLCA0OSwgMTMzLCAwLCA1MCwgMTM0LCAwLCA1MSwgMTM2LCAwLCA1MiwgMTM3LCAwLCA1MywgMTM5LCAwLCA1NCwgMTQyLCAwLCA1NSwgMTQ0LCAwLCA1NiwgMTQ1LCAwLCA1OCwgMTQ5LCAwLCA2MSwgMTU0LCAwLCA2MywgMTU2LCAwLCA2NSwgMTU5LCAwLCA2NiwgMTYxLCAwLCA2OCwgMTY0LCAwLCA2OSwgMTY3LCAwLCA3MSwgMTcwLCAwLCA3MywgMTc0LCAwLCA3NSwgMTc5LCAwLCA3NiwgMTgxLCAwLCA3OCwgMTg0LCAwLCA3OSwgMTg3LCAwLCA4MCwgMTg4LCAwLCA4MSwgMTkwLCAwLCA4NCwgMTk0LCAwLCA4NywgMTk4LCAwLCA4OCwgMjAwLCAwLCA5MCwgMjAzLCAwLCA5MiwgMjA1LCAwLCA5NCwgMjA3LCAwLCA5NCwgMjA4LCAwLCA5NSwgMjA5LCAwLCA5NiwgMjEwLCAwLCA5NywgMjExLCAwLCA5OSwgMjE0LCAwLCAxMDIsIDIxNywgMCwgMTAzLCAyMTgsIDAsIDEwNCwgMjE5LCAwLCAxMDUsIDIyMCwgMCwgMTA3LCAyMjEsIDAsIDEwOSwgMjIzLCAwLCAxMTEsIDIyMywgMCwgMTEzLCAyMjMsIDAsIDExNSwgMjIyLCAwLCAxMTcsIDIyMSwgMCwgMTE4LCAyMjAsIDEsIDEyMCwgMjE5LCAxLCAxMjIsIDIxNywgMiwgMTI0LCAyMTYsIDIsIDEyNiwgMjE0LCAzLCAxMjksIDIxMiwgMywgMTMxLCAyMDcsIDQsIDEzMiwgMjA1LCA0LCAxMzMsIDIwMiwgNCwgMTM0LCAxOTcsIDUsIDEzNiwgMTkyLCA2LCAxMzgsIDE4NSwgNywgMTQxLCAxNzgsIDgsIDE0MiwgMTcyLCAxMCwgMTQ0LCAxNjYsIDEwLCAxNDQsIDE2MiwgMTEsIDE0NSwgMTU4LCAxMiwgMTQ2LCAxNTMsIDEzLCAxNDcsIDE0OSwgMTUsIDE0OSwgMTQwLCAxNywgMTUxLCAxMzIsIDIyLCAxNTMsIDEyMCwgMjUsIDE1NCwgMTE1LCAyOCwgMTU2LCAxMDksIDM0LCAxNTgsIDEwMSwgNDAsIDE2MCwgOTQsIDQ1LCAxNjIsIDg2LCA1MSwgMTY0LCA3OSwgNTksIDE2NywgNjksIDY3LCAxNzEsIDYwLCA3MiwgMTczLCA1NCwgNzgsIDE3NSwgNDgsIDgzLCAxNzcsIDQzLCA4OSwgMTc5LCAzOSwgOTMsIDE4MSwgMzUsIDk4LCAxODMsIDMxLCAxMDUsIDE4NSwgMjYsIDEwOSwgMTg3LCAyMywgMTEzLCAxODgsIDIxLCAxMTgsIDE4OSwgMTksIDEyMywgMTkxLCAxNywgMTI4LCAxOTMsIDE0LCAxMzQsIDE5NSwgMTIsIDEzOCwgMTk2LCAxMCwgMTQyLCAxOTcsIDgsIDE0NiwgMTk4LCA2LCAxNTEsIDIwMCwgNSwgMTU1LCAyMDEsIDQsIDE2MCwgMjAzLCAzLCAxNjQsIDIwNCwgMiwgMTY5LCAyMDUsIDIsIDE3MywgMjA2LCAxLCAxNzUsIDIwNywgMSwgMTc4LCAyMDcsIDEsIDE4NCwgMjA4LCAwLCAxOTAsIDIxMCwgMCwgMTkzLCAyMTEsIDAsIDE5NiwgMjEyLCAwLCAxOTksIDIxMiwgMCwgMjAyLCAyMTMsIDEsIDIwNywgMjE0LCAyLCAyMTIsIDIxNSwgMywgMjE1LCAyMTQsIDMsIDIxOCwgMjE0LCAzLCAyMjAsIDIxMywgMywgMjIyLCAyMTMsIDQsIDIyNCwgMjEyLCA0LCAyMjUsIDIxMiwgNSwgMjI2LCAyMTIsIDUsIDIyOSwgMjExLCA1LCAyMzIsIDIxMSwgNiwgMjMyLCAyMTEsIDYsIDIzMywgMjExLCA2LCAyMzQsIDIxMCwgNiwgMjM1LCAyMTAsIDcsIDIzNiwgMjA5LCA3LCAyMzcsIDIwOCwgOCwgMjM5LCAyMDYsIDgsIDI0MSwgMjA0LCA5LCAyNDIsIDIwMywgOSwgMjQ0LCAyMDIsIDEwLCAyNDQsIDIwMSwgMTAsIDI0NSwgMjAwLCAxMCwgMjQ1LCAxOTksIDExLCAyNDYsIDE5OCwgMTEsIDI0NywgMTk3LCAxMiwgMjQ4LCAxOTQsIDEzLCAyNDksIDE5MSwgMTQsIDI1MCwgMTg5LCAxNCwgMjUxLCAxODcsIDE1LCAyNTEsIDE4NSwgMTYsIDI1MiwgMTgzLCAxNywgMjUyLCAxNzgsIDE4LCAyNTMsIDE3NCwgMTksIDI1MywgMTcxLCAxOSwgMjU0LCAxNjgsIDIwLCAyNTQsIDE2NSwgMjEsIDI1NCwgMTY0LCAyMSwgMjU1LCAxNjMsIDIyLCAyNTUsIDE2MSwgMjIsIDI1NSwgMTU5LCAyMywgMjU1LCAxNTcsIDIzLCAyNTUsIDE1NSwgMjQsIDI1NSwgMTQ5LCAyNSwgMjU1LCAxNDMsIDI3LCAyNTUsIDEzOSwgMjgsIDI1NSwgMTM1LCAzMCwgMjU1LCAxMzEsIDMxLCAyNTUsIDEyNywgMzIsIDI1NSwgMTE4LCAzNCwgMjU1LCAxMTAsIDM2LCAyNTUsIDEwNCwgMzcsIDI1NSwgMTAxLCAzOCwgMjU1LCA5OSwgMzksIDI1NSwgOTMsIDQwLCAyNTUsIDg4LCA0MiwgMjU0LCA4MiwgNDMsIDI1NCwgNzcsIDQ1LCAyNTQsIDY5LCA0NywgMjU0LCA2MiwgNDksIDI1MywgNTcsIDUwLCAyNTMsIDUzLCA1MiwgMjUyLCA0OSwgNTMsIDI1MiwgNDUsIDU1LCAyNTEsIDM5LCA1NywgMjUxLCAzMywgNTksIDI1MSwgMzIsIDYwLCAyNTEsIDMxLCA2MCwgMjUxLCAzMCwgNjEsIDI1MSwgMjksIDYxLCAyNTEsIDI4LCA2MiwgMjUwLCAyNywgNjMsIDI1MCwgMjcsIDY1LCAyNDksIDI2LCA2Niw'
destiny = 'tZwD5YPNlAvjtAwtfVQV0BPjtZwHfVQpjYPNlAQtfVQV0YPN3ZljtZwD3YPNlAPjtAmHfVQV0AljtZwHfVQp3YPNlAQpfVQV1YPN3BFjtZwD3YPNlAvjtBQRfVQV0AljtZmVfVQtmYPNlAQpfVQZ1YPN4AFjtZwD3YPNmBPjtBQLfVQV0AljtAQVfVQt4YPNlAQpfVQD2YPN5ZPjtZwD3YPN1ZPjtBGVfVQV0BPjtAGHfVQx0YPNlAQtfVQH5YPN5AvjtZwD4YPN2APjtBGtfVQV0BPjtAmVfVQRjZFjtZwD5YPN4ZFjtZGN0YPNlAQxfVQt3YPNkZQLfVQV1ZPjtBGZfVQRjBPjtZwHjYPN5AFjtZGN5YPNlAGNfVQx4YPNkZGNfVQV1ZPjtZGNjYPNkZGRfVQV1ZFjtZGNkYPNkZGVfVQV1ZFjtZGNlYPNkZGZfVQV1ZFjtZGN5YPNkZGpfVQV1ZvjtZGR2YPNkZwRfVQV1ZvjtZGVkYPNkZwZfVQV1ZljtZGV2YPNkZwLfVQV1ZljtZGZjYPNkZwtfVQV1APjtZGZ1YPNkZmRfVQV1APjtZGZ5YPNkZmZfVQV1APjtZGD0YPNkZmLfVQV1APjtZGHkYPNkAQNfVQV1AFjtZGH4YPNkAQDfVQV1AFjtZGLmYPNkAQLfVQV1AFjtZGL4YPNkAQxfVQV1AFjtZGpmYPNkAGVfVQV1AFjtZGp2YPNkAGZfVQV1AFjtZGp4YPNkAGHfVQV1AFjtZGt0YPNkAwNfVQV1AFjtZGxkYPNkAwHfVQV1AFjtZGx1YPNkAwtfVQV1AFjtZGx5YPNkAmVfVQV1AFjtZwNmYPNkAmHfVQV1AFjtZwN3YPNkAmxfVQV1AFjtZwRkYPNkBQVfVQV1AFjtZwR2YPNkBQHfVQV1AFjtZwR4YPNkBGNfVQV1AFjtZwVjYPNkBGLfVQV1AFjtZwVlYPNlZQNfVQV1AFjtZwV1YPNlZQVfVQV1AFjtZwV3YPNlZQDfVQV1AFjtZwZjYPNlZQLfVQV1AFjtZwZmYPNlZQuqPvNtVPOwo2kiqKWgLKOsnKWiozWfLJAeVQ0tJjbtVPNtVPNtVQV1AFjtZwH1YPNlAGHfVQV1ZljtZwHmYPNlAGZfVQV1ZFjtZwHkYPNlAGRfVQV0BFjtZwD5YPNlAQxfVQV0AljtZwD3YNbtVPNtVPNtVQV0AljtZwD1YPNlAQHfVQV0AFjtZwDmYPNlAQZfVQV0ZljtZwDkYPNlAQRfVQV0ZFjtZwZ5YPNlZmxfVQVmBFjtZwZ3YNbtVPNtVPNtVQVmAljtZwZ3YPNlZmHfVQVmAFjtZwZ1YPNlZmZfVQVmZljtZwZmYPNlZmRfVQVmZFjtZwZkYPNlZwxfVQVlBFjtZwV5YNbtVPNtVPNtVQVlAljtZwV3YPNlZwpfVQVlAFjtZwV1YPNlZwHfVQVlZljtZwVmYPNlZwZfVQVlZFjtZwVkYPNlZwRfVQVkBFjtZwR5YNbtVPNtVPNtVQVkBFjtZwR3YPNlZGpfVQVkAljtZwR1YPNlZGHfVQVkAFjtZwRmYPNlZGZfVQVkZljtZwRkYPNlZGRfVQVkZFjtZwN5YNbtVPNtVPNtVQVjBFjtZwN5YPNlZQpfVQVjAljtZwN3YPNlZQHfVQVjAFjtZwN1YPNlZQZfVQVjZljtZwNmYPNlZQRfVQVjZFjtZwNkYNbtVPNtVPNtVQR5BFjtZGx5YPNkBGxfVQR5AljtZGx3YPNkBGpfVQR5AFjtZGx1YPNkBGHfVQR5ZljtZGxmYPNkBGZfVQR5ZFjtZGxkYNbtVPNtVPNtVQR5ZFjtZGt5YPNkBQxfVQR4BFjtZGt3YPNkBQpfVQR4AljtZGt1YPNkBQHfVQR4AFjtZGtmYPNkBQZfVQR4ZljtZGtkYNbtVPNtVPNtVQR4ZFjtZGtkYPNkAmxfVQR3BFjtZGp5YPNkAmpfVQR3AljtZGp3YPNkAmHfVQR3AFjtZGp1YPNkAmZfVQR3ZljtZGpmYNbtVPNtVPNtVQR3ZFjtZGpkYPNkAmRfVQR2BFjtZGL5YPNkAwxfVQR2AljtZGL3YPNkAwpfVQR2AFjtZGL1YPNkAwHfVQR2ZljtZGLmYNbtVPNtVPNtVQR2ZljtZGLkYPNkAwRfVQR2ZFjtZGH5YPNkAGxfVQR1BFjtZGH3YPNkAGpfVQR1AljtZGH1YPNkAGHfVQR1AFjtZGHmYNbtVPNtVPNtVQR1ZljtZGHmYPNkAGRfVQR1ZFjtZGHkYPNkAQxfVQR0BFjtZGD5YPNkAQpfVQR0AljtZGD3YPNkAQHfVQR0AFjtZGD1YNbtVPNtVPNtVQR0ZljtZGDmYPNkAQZfVQR0ZFjtZGDkYPNkAQRfVQRmBFjtZGZ5YPNkZmxfVQRmAljtZGZ3YPNkZmpfVQRmAFjtZGZ1YNbtVPNtVPNtVQRmAFjtZGZmYPNkZmZfVQRmZljtZGZkYPNkZmRfVQRmZFjtZGV5YPNkZwxfVQRlBFjtZGV2YPNkZwLfVQRlAvjtZGV0YNbtVPNtVPNtVQRlAPjtZGV0YPNkZwVfVQRlZvjtZGVlYPNkZwNfVQRlZPjtZGVjYPNkZGtfVQRkBPjtZGR4YPNkZGLfVQRkAvjtZGR2YNbtVPNtVPNtVQRkAPjtZGR0YPNkZGDfVQRkZvjtZGRlYPNkZGVfVQRkZPjtZGRjYPNkZGNfVQRjBPjtZGN4YPNkZQtfVQRjAvjtZGN2YNbtVPNtVPNtVQRjAvjtZGN0YPNkZQDfVQRjAPjtZGNlYPNkZQVfVQRjZvjtZGNjYPNkZQNfVQRjZPjtBGtfVQx4YPN5BPjtBGLfVQx2YNbtVPNtVPNtVQx2YPN5APjtBGDfVQx0YPN5ZvjtBGVfVQxlYPN5ZPjtBGNfVQxjYPN4BPjtBQtfVQt4YPN4AvjtBQLfVQt2YPN4APjtBQDfPvNtVPNtVPNtBQDfVQtlYPN4ZvjtBQVfVQtjYPN4ZPjtBQNfVQp4YPN3BPjtAmtfVQp2YPN3AvjtAmLfVQp0YPN3APjtAmDfVQplYPN3ZvjXVPNtVPNtVPN3ZvjtAmNfVQpjYPN3ZPjtAwtfVQL4YPN2BPjtAwLfVQL2YPN2AvjtAwDfVQL0YPN2APjtAwVfVQLlYPN2ZvjtAwNfVQLjYNbtVPNtVPNtVQLjYPN1BPjtAGtfVQH4YPN1AvjtAGLfVQH2YPN1APjtAGDfVQH0YPN1ZvjtAGVfVQHlYPN1ZPjtAGNfVQHjYPN0BPjtAQtfPvNtVPNtVPNtAQtfVQD2YPN0AvjtAQLfVQD0YPN0APjtAQDfVQDlYPN0ZvjtAQVfVQDjYPN0ZPjtAQNfVQZ4YPNmBPjtZmtfVQZ2YPNmAvjXVPNtVPNtVPNmAvjtZmDfVQZ0YPNmAPjtZmVfVQZlYPNmZvjtZmNfVQZjYPNmZPjtZwtfVQV4YPNlBPjtZwLfVQV2YPNlAvjtZwDfVQV0YNbtVPNtVPNtVQV0YPNlZvjtZwVfVQVlYPNlZPjtZwNfVQVjYPNkBPjtZGtfVQR4YPNkAvjtZGLfVQR2YPNkAPjtZGDfVQR0YPNkZvjtZGVfPvNtVPNtVPNtZGVfVQRjYPNkZPjtZGNfVQtfVQtfVQtfVQLfVQLfVQLfVQDfVQDfVQDfVQVfVQVfVQVfVQNfVQNfVQNfVQNfVQNfVQxfPvNtVPNtVPNtZvjtZPjtZGLfVQDfVQNfVQV0YPN2YPNjYPNmZFjtBPjtZPjtZmtfVQRjYPNjYPN0AFjtZGVfVQNfVQHmYPNkAPjtZPjXVPNtVPNtVPN2ZPjtZGpfVQNfVQL3YPNkBFjtZPjtAmDfVQVkYPNjYPN4ZvjtZwZfVQNfVQt5YPNlAFjtZPjtBGLfVQV3YPNjYPNkZQZfPvNtVPNtVPNtZwxfVQNfVQRkZFjtZmRfVQNfVQRkBPjtZmLfVQNfVQRlZPjtAQRfVQNfVQRlZFjtAQLfVQNfVQRlZvjtAGRfVQNfVQRlZljXVPNtVPNtVPN1AvjtZPjtZGV0YPN2ZFjtZPjtZGV1YPN2AvjtZPjtZGV2YPN3ZFjtZPjtZGV3YPN3AvjtZFjtZGV4YPN4ZFjtZFjtZGV5YNbtVPNtVPNtVQt2YPNkYPNkZmNfVQxkYPNkYPNkZmRfVQx2YPNkYPNkZmVfVQRjZFjtZFjtZGZmYPNkZQLfVQRfVQRmAPjtZGRkYPNkYNbtVPNtVPNtVQRmAFjtZGR2YPNkYPNkZmLfVQRlZFjtZFjtZGZ2YPNkZwHfVQVfVQRmAljtZGZjYPNlYPNkZmpfVQRmAFjtZljtZGZ3YNbtVPNtVPNtVQRmBFjtZljtZGZ4YPNkAQDfVQZfVQRmBPjtZGD5YPN0YPNkZmtfVQR1ZljtAPjtZGZ5YPNkAGtfVQHfVQRmBFjtZGLmYNbtVPNtVPNtVQHfVQRmBFjtZGL3YPN1YPNkAQNfVQR3ZvjtAvjtZGDjYPNkAmpfVQLfVQR0ZPjtZGtkYPN3YPNkAQRfVQR4AvjtAljXVPNtVPNtVPNkAQRfVQR4BFjtZGNfVQRmAljtZGxkYPNkZljtZGZlYPNkBGDfVQR2YPNkZwpfVQR5AvjtZGxfVQRlZFjtZGx4YPNlZvjXVPNtVPNtVPNkZGLfVQVjZPjtZwHfVQRkZFjtZwNmYPNlBPjtZGN2YPNlZQHfVQZkYPNkZQRfVQVjAljtZmDfVQx1YPNlZQxfVQZ3YNbtVPNtVPNtVQxjYPNlZGVfVQDjYPN4AFjtZwR0YPN0ZljtBQNfVQVkAvjtAQLfVQp1YPNlZGtfVQD5YPN2BFjtZwVkYPN1ZvjtAwDfPvNtVPNtVPNtZwVmYPN1AFjtAGxfVQVlAPjtAGpfVQD5YPNlZwHfVQLjYPN0AljtZwV2YPN2APjtAQDfVQVlAljtAwpfVQDlYPNlZwtfPvNtVPNtVPNtAmRfVQZ5YPNlZwxfVQp0YPNmAljtZwZjYPN3BPjtZmDfVQVmZFjtBQRfVQZlYPNlZmRfVQt1YPNlBFjtZwZlYPN4BPjXVPNtVPNtVPNlAljtZwZmYPN5ZvjtZwDfVQVmAPjtBGHfVQVlYPNlZmHfVQx5YPNkBFjtZwZ2YPNkZQVfVQR3YPNlZmpfVQRjAvjtZGDfPvNtVPNtVPNtZwZ4YPNkZQxfVQRlYPNlZmxfVQRkZvjtZGVfVQV0ZPjtZGR2YPNkZvjtZwDjYPNkZGxfVQRlYPNlAQRfVQRlZljtZGVfPvNtVPNtVPNtZwDkYPNkZwpfVQRlYPNlAQVfVQRmZPjtZGVfVQV0ZvjtZGZ0YPNkZvjtZwDmYPNkZmtfVQRlYPNlAQZfVQR0ZFjtZGZfPvNtVPNtVPNtZwD0YPNkAQHfVQRmYPNlAQDfVQR0BFjtZGZfVQV0AFjtZGHlYPNkZljtZwD1YPNkAGLfVQRmYPNlAQLfVQR2ZPjtZGZfPvNtVPNtVPNtZwD2YPNkAwZfVQRmYPNlAQpfVQR2AljtZGZfVQV0AljtZGpkYPNkZljtZwD4YPNkAmHfVQR0YPNlAQtfVQR3BPjtZGHfPvNtVPNtVPNtZwD5YPNkBQVfVQR2YPNlAQxfVQR4AFjtZGtfVQV1ZPjtZGt5YPNkBFjtZwHjYPNkBGVfVQVjYPNlAGRfVQR5AvjtZwRfPvNtVPNtVPNtZwHkYPNkBGxfVQVlYPNlAGVfVQVjZljtZwZfVQV1ZvjtZwN2YPNlAPjtZwHmYPNlZGNfVQV1YPNlAGZfVQVkZljtZwpfPvNtVPNtVPNtZwH0YPNlZGpfVQV4YPNlAGDfVQVlZPjtZwxfVQV1AFjtZwV0YPNmZPjtZwH1YPNlZwpfVQZ5YPNlAGHfVQVlBFjtAGZfPvNtVPNtVPNtZwH1YPNlZmRfVQL3YPNlAGHfVQVmZljtBQRfVQV1AFjtZwZ0YPN5AFjtZwH1YPNlZmLfVQRjBFjtZwH1YPNlZmtfVQRlZljXVPNtVPNtVPNlAGHfVQV0ZPjtZGZ3YPNlAGHfVQV0ZvjtZGHkYPNlAGHfVQV0APjtZGL1YPNlAGHfVQV0AvjtZGp5YPNlAGHfVQV0BPjXVPNtVPNtVPNkBGZfVQV1AFjtZwD5YPNlZQpfVQV1AFjtZwHkYPNlZwRfVQV1AFjtZwHmYPNlZmHfVQV1AFjtZwH1YPNlAS0XPvNtVPOxMJLtL2u1ozfbqJkcp3DfVUA0MKNcBtbtVPNtVPNtVUWyqUIlovOgLKNboTSgLzEuVTx6VUIfnKA0J2x6VTxtXlOmqTIjKFjtpzShM2HbZPjtoTIhXUIfnKA0XFjtp3EypPxcPtbtVPNtnJLtXTAioT9lGJSjIUyjMFN9CFNkXGbXVPNtVPNtVPOwnUIhn3ZtCFOwnUIhnluwo2kipz1upS9lLJyhLz93YPNmXDbtVPNtMJkcMvNbL29fo3WALKOHrKOyVQ09VQVcBtbtVPNtVPNtVTAbqJ5eplN9VTAbqJ5eXTAioT9loJSjK2qlLKymL2SfMFjtZlxXVPNtVTIfp2H6PvNtVPNtVPNtL2u1ozgmVQ0tL2u1ozfbL29fo3IloJSjK2ylo25voTSwnljtZlxXPvNtVPOlMJDtCFOoKDbtVPNtM3WyMJ4tCFOoKDbtVPNtLzk1MFN9VSgqPvNtVPOzo3VtL2u1ozftnJ4tL2u1ozgmBtbtVPNtVPNtVUWyMP5upUOyozDbL2u1ozgoZS0cPvNtVPNtVPNtM3WyMJ4hLKOjMJ5xXTAbqJ5eJmSqXDbtVPNtVPNtVTWfqJHhLKOjMJ5xXTAbqJ5eJmWqXDbXVPNtVTk1qSf6YPNjYPNjKFN9VTWfqJHXVPNtVTk1qSf6YPNjYPNkKFN9VTqlMJIhPvNtVPOfqKEoBvjtZPjtZy0tCFOlMJDXVPNtVUWyqUIlovOfqKDXPtccMvOsK25uoJIsKlN9CFNaK19gLJyhK18aBtbtVPNtV21unJ4bXDbtVPNtpzIuMTEuqTRbXFNtVPNXVPNXVPNtVPZtp3EupaDtLFO0nUWyLJDtqTuuqPO3nJkfVUOypzMipz0toJ90nJ9hVTEyqTIwqTyiotbtVPNtqPN9VUEbpzIuMTyhMl5HnUWyLJDbqTSlM2I0CJqyovxXVPNtVUDhMTSyoJ9hVQ0tIUW1MDbtVPNtqP5mqTSlqPtcPvNtVPNXVPNtVPAupUNhpaIhXTuip3D9WmR5Zv4kAwthBP4kZQZaYUOipaD9WmtjZQNaYPOxMJW1Mm1HpaIyYPO1p2IspzIfo2SxMKVtCFOTLJkmMFxXVPNtVTSjpP5lqJ4bLJExpzImp2yjYTSxMUWyp3Ajo3W0YPOxMJW1Mm1HpaIyYPO0nUWyLJEyMQ1HpaIyYPO1p2IspzIfo2SxMKVtCFOTLJkmMFxXVPNtVN=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))