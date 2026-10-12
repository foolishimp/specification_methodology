# Operator note: first-month cost comparison

Start by binding `cost-brief/source-v1` and the current documentary write grant. This fixture is in `stdo_3/build_tenants/codex/qualification/T2_T6/TASKS.md` at commit `e5ac730699afcd1fc6a1f610d2186c63ac328ca3`, under **D Source, Revision 1**. Preserve that revision with the calculation.

The selected interval is 30 days, with two nodes continuously running 24 hours per day: **2 × 24 × 30 = 1,440 node-hours**. Outbound traffic is 40 GB for the whole interval; each backup quote also covers that whole interval. Currency is AUD, with 100 cents per dollar.

| Offering | Compute quote → AUD/node-hour | Backup AUD/interval | Outbound quote → AUD/GB |
|---|---|---:|---|
| Harbor | 6 cents → 0.06 | 18 | 4 cents → 0.04 |
| Cove | 10 cents → 0.10 | 3 | 2.5 cents → 0.025 |

For each offering separately, calculate **node-hours × compute rate + interval backup + GB × outbound rate**:

| Offering | Compute AUD | Backup AUD | Outbound AUD | Total AUD | AUD 160 ceiling |
|---|---:|---:|---:|---:|---|
| Harbor | 1,440 × 0.06 = 86.40 | 18.00 | 40 × 0.04 = 1.60 | **106.00** | Below by 54.00 |
| Cove | 1,440 × 0.10 = 144.00 | 3.00 | 40 × 0.025 = 1.00 | **148.00** | Below by 12.00 |

The included charges are compute, backup and outbound traffic. Tax, discounts, currency conversion and other charges are excluded by this fixture. Preserve those exclusions as assumptions whenever carrying the estimate forward. Provider selection remains the comparison owner's decision.

At the producer/consumer seam, Harbor's `rate = 6` means **AUD cents per node-hour**, scoped to Harbor/source-v1. A consumer expecting AUD dollars per node-hour receives **0.06**, using the declared 100:1 conversion, with the offering, source revision and original unit retained. Record that directional conversion; matching numeric field shapes cannot settle units. Stop the affected join if its source identity or unit meaning cannot be resolved.

For a changed assumption, record the old value, proposed value, affected estimate and owner route in admitted documentary output first. The comparison owner owns the selected interval, node count, traffic, excluded-charge assumptions and ceiling. A changed quote or quote unit returns to the source contract's owner through the assigning root. The fixture supplies no personal identity for either owner. Obtain an owner-bound successor or instruction before relying on changed premises; retain source-v1 and its surviving calculation. For a new interval, recompute node-hours from its admitted days and node count, and acquire backup and traffic premises for that interval rather than silently prorating whole-interval quotes.

This activation permits only `runs/reader/rc2/OPERATOR_NOTE.md` and `runs/reader/rc2/RETURN.md` under the assigned T2_T6 directory. A later analyst must bind their own current territory before writing. Missing or out-of-territory authority stops the affected write. Return the comparison for assessment; a correct cost judgment supplies no deployment grant. Stop before cloud-account use, contact, purchase, payment, network access, deployment or common-source mutation.

Method entry is the installed RC2 [Standards Library](</Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/README.md>). Its responsibility routes are [semantic resolution and change intake](</Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/SPEC_METHOD.md>), [authority conservation](</Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#authority>) and the [Worker and Reviewer frames](</Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md>).
