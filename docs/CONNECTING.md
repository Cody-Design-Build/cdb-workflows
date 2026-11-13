# Connect an assistant to JobTread

Configure your assistant’s MCP connection separately from installing this library’s skills. Prefer direct OAuth authorization against the official endpoint, `https://api.jobtread.com/mcp`. Each person signs in with their own JobTread account; no shared or copied tokens are required.

## Prepare your account and client

Use an MCP client with remote Streamable HTTP and OAuth support. Confirm that your JobTread administrator permits the integration and the account actions you need. Client support changes between versions; the examples below follow the linked upstream documentation, not a completed compatibility test across every client version.

JobTread’s official references are:

- [AI Connector overview](https://www.jobtread.com/integrations/ai-connector)
- [Connect AI tools to JobTread](https://app.jobtread.com/help/ai-connect-ai-tools-to-jobtread)
- [Claude integration](https://app.jobtread.com/help/ai-claude-integration)
- [ChatGPT integration](https://app.jobtread.com/help/ai-chat-gpt-integration)

The help pages may require an authenticated browser. Opening the MCP URL in a browser can redirect to help; that is not an MCP discovery or authentication test. Use your client’s MCP connection flow.

## Configure one client

Merge the relevant entry into your existing configuration; do not overwrite unrelated servers or settings. Configuration writes alone do not establish successful OAuth or tool discovery. Do not add an `Authorization` header containing a token copied from another client.

### Codex

Add this table to `~/.codex/config.toml`, then authorize the named server:

```toml
[mcp_servers.jobtread]
url = "https://api.jobtread.com/mcp"
```

```sh
codex mcp login jobtread
codex mcp list
```

You can also add the endpoint with `codex mcp add jobtread --url https://api.jobtread.com/mcp`. Use `/mcp` inside Codex to inspect active tools. See [Codex MCP configuration](https://developers.openai.com/codex/mcp).

### Claude Code

Add a user-scoped HTTP connection, then start browser authorization:

```sh
claude mcp add --scope user --transport http \
  jobtread https://api.jobtread.com/mcp
claude mcp login jobtread
claude mcp list
```

Inside an interactive Claude Code session, `/mcp` also offers authentication and connection status. For a reviewed project configuration, the equivalent `.mcp.json` shape is:

```json
{
  "mcpServers": {
    "jobtread": {
      "type": "http",
      "url": "https://api.jobtread.com/mcp"
    }
  }
}
```

Prefer user scope when you do not intend to share a server definition. Claude Desktop and Claude’s web connector have different setup interfaces; follow JobTread’s Claude help instead of assuming this CLI command applies there. See [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp).

### Hermes

Merge this entry into your active profile’s `config.yaml` (default: `~/.hermes/config.yaml`):

```yaml
mcp_servers:
  jobtread:
    url: "https://api.jobtread.com/mcp"
    auth: oauth
```

Run the OAuth login, then start a new session or reload MCP:

```sh
hermes mcp login jobtread
hermes chat
```

Use `/reload-mcp` in an existing supported session. See the upstream [Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) and [configuration reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/mcp-config-reference.md).

### OpenCode

Current upstream V2 documentation uses `mcp.servers`, not the older direct `mcp` server map. Add a global connection with the CLI:

```sh
opencode mcp add jobtread --global --url https://api.jobtread.com/mcp
opencode mcp auth jobtread
opencode mcp list
```

The current JSON configuration shape is:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
      "jobtread": {
        "type": "remote",
        "url": "https://api.jobtread.com/mcp"
      }
    }
  }
}
```

Remote OAuth is enabled by default. In OpenCode, `/mcps` opens server status and sign-in. Match your installed version’s schema; V2 uses `disabled`, not `enabled`, when disabling a server. See [OpenCode MCP servers](https://opencode.ai/docs/mcp-servers).

### omp

Merge this entry into the active profile’s native MCP file. The default user path is `~/.omp/agent/mcp.json`; named profiles use `~/.omp/profiles/profile_name/agent/mcp.json`:

```json
{
  "mcpServers": {
    "jobtread": {
      "type": "http",
      "url": "https://api.jobtread.com/mcp"
    }
  }
}
```

Inside omp, run `/mcp reauth jobtread`, complete browser consent, and inspect `/mcp list`. Use `/mcp reload` after configuration changes. Let omp manage OAuth credentials outside the shared definition; do not manually insert credential IDs or tokens. See the upstream [omp MCP configuration guide](https://github.com/can1357/oh-my-pi/blob/main/docs/mcp-config.md).

## Complete browser consent

Review the browser’s destination, JobTread identity, organization, and requested permissions before approving. Cancel if the account, organization, or access level is wrong. Request the permissions your authorized work requires; do not silently downgrade CDB’s approved full-access setup or treat that access as approval for a specific business change.

Keep the client running until its loopback OAuth callback completes. When working remotely, follow the client’s documented callback or SSH-forwarding procedure. A callback URL can contain a temporary authorization code: paste it only into that client’s own authorization prompt, never into chat, tickets, or this repository.

Your client stores its own OAuth credentials locally. Do not copy Claude, ChatGPT, or another person’s tokens into an agent configuration. Keep authentication stores and browser consent details out of version control.

## Verify the connection without changing records

Verify the following sequence in each client you intend to use:

1. Complete OAuth and confirm that the client reports a connected server.
2. Discover every exposed MCP tool, including its complete input schema and description. Store captures privately until reviewed for public release.
3. Read the live grant’s organization and allowed actions. Tool availability and grant permissions are different: a general `query` tool can describe mutations your grant cannot execute.
4. Discover the live schema for the reads you need. Compare it with bundled reference snapshots; do not guess operation names, fields, IDs, filters, or pagination.
5. Read a minimal, authorized organization/account/project record. Confirm the expected organization and exact target without publishing its IDs or contents.
6. Restart the client or disconnect/reconnect, rediscover tools, and repeat the harmless read. Confirm saved authorization works; renewed consent may be necessary after expiry, revocation, or permission changes.

When the live tool description confirms the bundled `query` syntax, these read-only requests inspect permissions and schema:

```json
{
  "query": {
    "currentGrant": {
      "allowedActions": {},
      "organization": {"id": {}, "name": {}}
    }
  }
}
```

```json
{"query":{"schema":{"$":{"path":"root","search":"job"}}}}
```

The first request returns live organization data, so keep the response private. The second discovers possible job reads; inspect the returned schemas before selecting a minimal real record. Read `skills/jobtread/references/query-tool.md` for the captured upstream syntax, but treat live discovery as authoritative.

Record which client/version, transport, and verification steps succeeded. Report missing permissions or untested capabilities rather than claiming complete workflow coverage. Never create, issue, send, pay, or delete records merely to verify connectivity.

## Reconnect or resolve permission failures

Use the client’s sign-in or reauthorization flow if it reports expired or revoked authorization. Check the active profile, exact endpoint, account, and live grant before changing anything. A permission denial is not evidence that a tool is absent, and reconnecting does not expand server-side permissions.

After reconnecting, rediscover tools and read the exact target. If a business write had an uncertain result, reconcile it through a read before retrying. Never blindly repeat a create, payment, send, or delete.

## Use a hosted ChatGPT or Claude assistant

Hosted assistants cannot use links on your computer. Connect JobTread through that product's official connector using the JobTread help linked above, then provide the reviewed workflow instructions through the product's supported project instructions, knowledge files or conversation attachments.

Download a reviewed repository release from GitHub. Provide `skills/jobtread/SKILL.md`, its query procedure and the reference for the task. Include the budget-writing and catalog skills when relevant. Relative file links do not guarantee that a hosted assistant can retrieve dependencies: attach those Markdown references too, or have it fetch and read the corresponding public repository files before acting. Keep these as distributed copies of a named release, never independently maintained policy.

Tell the assistant to follow CDB's attached JobTread procedures, discover its actual connector schemas and stop before unapproved writes. Confirm it can read the supplied instructions and complete the read-only connection checklist. A GitHub URL alone does not install instructions or establish MCP access. Updating the local checkout does not refresh a hosted project's attachments; replace them deliberately when adopting a new release.

This repository does not claim a native JobTread skill import or a universal hosted-assistant upload format.

## Reuse an existing local Linux gateway only when needed

A previously configured Linux gateway can adapt the official OAuth MCP to a local authenticated HTTP endpoint and a stdio client. It is optional, belongs to one OS user, and is not required for any client that can authorize the official server directly. This repository does not ship or install that gateway.

The inspected local adapter consists of `~/.local/share/jobtread-mcp/gateway.py`, `client.py`, and a pinned `requirements.lock`. The inspected lock pins FastMCP 4.1.4. `gateway.py` uses FastMCP’s upstream OAuth client, encrypts saved OAuth material under `~/.config/jobtread`, and binds a bearer-protected proxy to `127.0.0.1:8766`. `client.py` reads the local bearer credential from a protected file and proxies stdio to `http://127.0.0.1:8766/mcp`; it does not contain JobTread business tools.

If that adapter already exists and works, configure a stdio server using its existing environment’s Python executable and the absolute path to `client.py`. Do not use system Python unless it has the adapter’s pinned dependencies. Substitute your actual home path for `/home/your_user` in this example:

```json
{
  "mcpServers": {
    "jobtread": {
      "type": "stdio",
      "command": "/home/your_user/.local/share/jobtread-mcp/.venv/bin/python",
      "args": ["/home/your_user/.local/share/jobtread-mcp/client.py"]
    }
  }
}
```

That entry shape applies to omp and Claude Code. Codex uses `command` and `args` under `[mcp_servers.jobtread]`; Hermes uses them under `mcp_servers.jobtread`. OpenCode V2 uses `type: "local"` with a single `command` array containing the executable and arguments under `mcp.servers.jobtread`. Choose either a direct or adapter entry for the same connection, not both.

Do not copy this machine’s service files, grants, tokens, encryption keys, or authorization history to another machine or person. Keep credential files mode `600` and their directories mode `700`. Never bind the proxy to a LAN/public interface. An adapter deployment additionally requires checking rejection of unauthenticated requests, authenticated discovery/read, and restart/reconnect. Source inspection is not proof those runtime checks passed on your installation.

The filesystem skill installer only creates discovery links. It never creates credentials or performs gateway installation, service setup, or OAuth consent.
