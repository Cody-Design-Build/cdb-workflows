# Google Workspace authorization

Use the assistant's maintained Google Workspace/Gmail connector and its current official setup instructions. Discover supported connection options instead of inventing commands or installing a custom gateway. This library installs no Google connector or OAuth application.

Each person authorizes their own account through the connector's secure consent flow. Confirm mailbox and needed permissions. Never paste passwords, tokens or callback codes into chat or copy another client's credentials. Keep credentials in the connector's private storage outside source control. Delegated access needs separate authorization.

Installation, authorization, tool discovery and a successful harmless read are separate milestones. Discover live read/draft/send schemas, verify account, and perform a minimal authorized read. No send, draft creation or mailbox mutation is needed to test connection. Reconnect and repeat a harmless read before claiming saved authorization works. Missing draft support never authorizes sending.

Load [business-email](../skills/business-email/SKILL.md) for email tasks. Its final-preview and separate explicit send-confirmation gate applies regardless of provider/client. No mailbox identities, tokens, private examples or runtime evidence belong in this library.
