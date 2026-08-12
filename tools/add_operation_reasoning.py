"""Place contextual reasons and Mathematical Moves links before every equation."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
GUIDE = "../../MATHEMATICAL_MOVES.md"


def move(anchor, label):
    return f"[{label}]({GUIDE}#{anchor})"


REASONS = {
2: [
    f"{move('brackets', 'Brackets')} keep tiger weight, speed, and age together without pretending they should be added; each observation must remain recoverable.",
    f"{move('indices', 'Subscripts')} give each retained feature an address. The dots mean the same pattern continues until feature n; they do not hide another operation.",
    f"{move('equals', 'The equals sign')} says that **x** is our short name for this complete ordered list.",
],
3: [
    f"{move('subtraction', 'Subtracting')} tiger height from tiger height and tiger speed from tiger speed isolates each like-for-like disagreement. Adding would measure a total, not a gap.",
    f"{move('powers', 'Squaring')} stops a smaller and larger feature from cancelling and makes a large mismatch count more strongly. Absolute value could stop cancellation too, but would produce a different geometry in which many small misses and one large miss trade differently.",
    f"{move('summation', 'Adding the squared disagreements')} lets every retained feature contribute to one separation. Multiplying would let one perfect feature match erase all other disagreement by making the product zero.",
    f"{move('square-root', 'The square root')} returns the accumulated squared separation to the features' ordinary scale; it is omitted when squared distance itself is all an algorithm needs.",
],
4: [
    f"{move('subtraction', 'Destination minus starting point')} is forced because we want the change that would carry **a** to **b**, not their combined location.",
    f"{move('negative-sign', 'A negative coordinate')} keeps direction: −2 means move two units opposite that axis, not that the movement has an impossible size.",
    f"{move('addition', 'Adding the change back')} is the check: starting place plus the discovered movement must recover the destination.",
],
5: [
    f"{move('multiplication', 'Multiplication')} lets each clue's importance scale that clue. A zero weight silences it; a weight of three makes it count three times.",
    f"{move('addition', 'Addition')} combines the scaled clues because they are separate contributions to the same judgment. Multiplying them would make any zero clue erase the entire decision and would claim interaction we never asked for.",
    f"{move('equals', 'Each equals sign')} records that the verbal judgment, its arithmetic recipe, and its final score are three descriptions of the same result.",
],
7: [
    f"{move('arrows', 'The arrow')} means “represent this token as,” not equality: a word and its numerical representation are different kinds of object.",
    f"{move('membership', 'The membership sign')} says the embedding is allowed to live among d-coordinate real vectors.",
    f"{move('powers', 'The superscript d')} counts coordinate slots here; it is dimension, not an instruction to raise each number to a power.",
],
9: [
    f"{move('exponential', 'Exponentiation')} makes every raw score positive while preserving order and turning score gaps into stable ratios. Squaring would make a large negative score look strong; clipping would destroy gap information.",
    f"{move('summation', 'The sum')} gathers every candidate's positive weight because all candidates must share one unit of attention. A product would not describe a total available amount.",
    f"{move('division', 'Dividing by that total')} converts each weight into its share. Without it, multiplying every score scale would change the amount of information mixed rather than only its distribution.",
],
10: [
    f"{move('dot-product', 'The dot product')} multiplies query height-need by key height-offer, stripe-need by stripe-offer, and so on, then adds those aligned agreements into one relevance score.",
    f"{move('multiplication', 'Multiplication inside the dot product')} is required because a query feature should matter only when the matching key feature is present too; addition would reward a key for merely being large on unrelated features.",
    f"{move('summation', 'The first sum')} combines feature-level evidence into one match. The second sum combines each source's value after its attention weight scales how loudly that source contributes.",
],
11: [
    f"{move('concatenation', 'Concatenation')} keeps the grammar expert, reference expert, and distance expert side by side. Adding them immediately would erase which head supplied which evidence.",
    f"{move('multiplication', 'Multiplication by the output matrix')} lets the model learn how those preserved expert coordinates should interact; a fixed sum would impose the same mixture everywhere.",
],
12: [
    f"{move('multiplication', 'Each matrix multiplication')} lets learned weights decide how strongly one incoming feature should affect each hidden or outgoing feature.",
    f"{move('addition', 'Adding a bias')} lets a detector have a baseline threshold even when all incoming features are zero; multiplication alone must always map zero input to zero output.",
    f"{move('function-application', 'The activation function')} bends the intermediate result. Without that nonlinearity, the two matrix stages collapse into one linear transformation.",
],
13: [
    f"{move('addition', 'Addition')} preserves the old message **x** and treats the block as a proposed change **F(x)**. Replacing x would force every block to reconstruct all useful old information.",
    f"{move('function-application', 'F(x)')} says the proposed change depends on this exact incoming representation rather than being one fixed correction for every token.",
],
14: [
    f"{move('mean', 'Summing and dividing by d')} finds the token's average feature level. A raw sum would grow merely because the representation has more coordinates.",
    f"{move('subtraction', 'Subtracting the mean')} asks how each feature differs from this token's centre; addition would move the whole pattern farther from centre.",
    f"{move('variance', 'Squaring and averaging those differences')} measures spread without quieter and louder features cancelling each other.",
    f"{move('square-root', 'The square root')} returns variance to ordinary feature scale, and {move('division', 'division by that spread')} removes arbitrary volume while preserving relative shape.",
    f"Adding ε is a safety floor: when every feature is identical, spread is zero and division would be undefined. See {move('addition', 'addition')} and {move('division', 'division')}.",
],
15: [
    f"{move('gradient', 'The gradient')} collects one local loss sensitivity for every adjustable weight so the whole parameter state receives coordinated advice.",
    f"{move('negative-sign', 'The minus sign')} reverses the gradient because the gradient points toward increasing loss and learning wants the locally decreasing direction.",
    f"{move('multiplication', 'Multiplying by η')} chooses how much of that direction to trust. Without η, the gradient's magnitude would dictate the whole step even when it is too large or too small.",
    f"The update arrow means “replace the old parameter state with this new one”; it is an action, not symmetric equality. See {move('arrows', 'arrows')}.",
],
17: [
    f"{move('division', 'Division')} turns a tiger count into a share of comparable encounters. The count alone grows when we watch longer even if the underlying chance is unchanged.",
    f"{move('probability', 'Probability')} preserves several possible causes as parts of one whole instead of forcing certainty from incomplete evidence.",
],
18: [
    f"{move('conditional-bar', 'The conditional bar')} deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.",
    f"{move('equals', 'Equality')} renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.",
],
19: [
    f"{move('logarithm', 'The logarithm')} is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.",
    f"{move('negative-sign', 'The negative sign')} reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.",
    f"Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.",
],
20: [
    f"{move('multiplication', 'Multiplying each surprise by pᵢ')} lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.",
    f"{move('summation', 'Summing')} combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.",
    f"{move('logarithm', 'The log')} still converts probability products into additive information, and {move('negative-sign', 'the minus sign')} keeps that information nonnegative.",
],
21: [
    f"{move('logarithm', '−log qᵢ')} charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.",
    f"{move('multiplication', 'Multiplying by pᵢ')} asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.",
    f"{move('summation', 'The sum')} forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.",
],
22: [
    f"{move('subtraction', 'The numerator subtracts')} old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.",
    f"{move('division', 'Division by the weight nudge')} converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.",
    f"{move('limit', 'The limit')} lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.",
],
23: [
    f"Each {move('derivative', 'derivative')} is a local conversion rate: loss per y, y per x, and x per weight.",
    f"{move('multiplication', 'Multiplying the rates')} is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.",
],
24: [
    f"{move('partial-derivative', 'The partial derivative')} measures one local edge while other inputs are held fixed.",
    f"{move('multiplication', 'Multiplying child blame by edge sensitivity')} passes downstream responsibility through that edge; either factor being zero should block that path.",
    f"{move('summation', 'Summing over children')} reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.",
],
25: [
    f"{move('indices', 'The time indices')} distinguish the parameter state before update t from the state after it.",
    f"{move('gradient', 'The gradient')} supplies one local uphill sensitivity for each parameter; {move('negative-sign', 'the minus sign')} reverses that direction toward lower loss.",
    f"{move('multiplication', 'Multiplying by η')} supplies the missing travel distance. A direction alone does not say whether to move one millimetre or one kilometre.",
],
26: [
    f"{move('summation', 'The sum')} lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.",
    f"{move('division', 'Dividing by |B|')} asks for advice per example, so merely inviting twice as many witnesses does not double the update.",
    f"{move('membership', 'i ∈ B')} restricts the sum to examples actually selected for this mini-batch; {move('cardinality', '|B|')} means the number of those examples.",
],
27: [
    f"{move('gradient', 'gₜ')} gives direction but not distance.",
    f"{move('multiplication', 'Multiplying by ηₜ')} turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.",
    f"{move('negative-sign', 'Subtraction')} moves opposite the locally uphill gradient rather than making loss rise faster.",
],
28: [
    f"{move('multiplication', 'Multiplying old velocity by β')} fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.",
    f"{move('addition', 'Adding the new gradient')} lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.",
    f"The final {move('multiplication', 'η scaling')} chooses travel distance and {move('negative-sign', 'the minus sign')} turns remembered uphill direction into a downhill update.",
],
29: [
    f"{move('variance', 'Variance')} describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.",
    f"{move('division', 'Dividing by the number of incoming signals')} makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.",
    f"{move('approximation', 'The approximately sign')} admits a design target rather than claiming every finite random sample has exactly this variance; see {move('equals', 'equality')} for the stronger claim it avoids.",
],
30: [
    f"{move('multiplication', 'Wx')} lets every learned input weight scale and mix its matching feature; {move('addition', 'adding b')} supplies a learnable baseline.",
    f"{move('function-application', 'Applying φ')} bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.",
],
31: [
    f"{move('subtraction', 'Unseen loss minus training loss')} isolates how much performance deteriorates beyond memorized examples. Adding the losses would measure total error, not the transfer gap.",
    f"The order matters: a positive answer naturally means unseen cases are worse. Reversing the subtraction would reverse that interpretation.",
],
32: [
    f"{move('addition', 'Addition')} puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.",
    f"{move('norm', 'The squared norm')} combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.",
    f"{move('multiplication', 'λ scales the penalty')} because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.",
],
33: [
    f"{move('union', 'Union')} says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.",
    f"Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.",
],
34: [
    f"{move('expectation', 'Expectation')} weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.",
    f"{move('function-application', 'fθ(x)')} feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.",
    f"The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.",
],
35: [
    f"{move('arrows', 'Arrows')} preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.",
    f"{move('gradient', 'The gradient stage')} changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.",
],
36: [
    f"{move('equals', 'The first equality')} defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.",
    f"{move('arg-max', 'Arg max')} returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.",
    f"{move('symbol-decorations', 'The star')} marks the selected winner; it is a label on a and b, not multiplication or exponentiation.",
],
37: [
    f"{move('membership', 'E ∈ ℝ')} states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.",
    f"{move('indices', 'E[i]')} treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.",
    f"{move('multiplication', 'One-hot multiplication')} gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.",
],
38: [
    f"{move('addition', 'Addition')} overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.",
    f"{move('indices', 'The shared index i')} forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.",
],
39: [
    f"{move('cases', 'Cases')} are forced because visible and forbidden positions obey genuinely different rules.",
    f"{move('inequalities', 'j ≤ i and j > i')} divide earlier-or-current keys from future keys for query position i.",
    f"Zero leaves an allowed attention score unchanged. {move('negative-sign', 'Negative infinity')} makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.",
],
40: [
    f"{move('brackets', 'Parentheses')} keep each ordered token sequence intact; summing the tokens would destroy both identity and order.",
    f"{move('indices', 'The shifted indices')} remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.",
],
41: [
    f"{move('multiplication', 'Multiplication by Wvocab')} lets every contextual feature contribute a learned amount to every vocabulary candidate's score.",
    f"{move('addition', 'The bias')} gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.",
    f"The index i selects one output candidate; it does not mean the token with the largest ID should win. See {move('indices', 'indices')}.",
],
42: [
    f"{move('exponential', 'Exponentials')} create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.",
    f"{move('summation', 'Summing all weights')} measures the whole amount to be shared, and {move('division', 'division')} turns each candidate's weight into a probability share.",
    f"{move('logarithm', 'The log')} turns the probability assigned to the observed token into additive information cost; {move('negative-sign', 'the minus sign')} makes low probability expensive and certainty cost zero.",
],
43: [
    f"{move('division', 'Dividing every logit by T')} changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.",
    f"{move('exponential', 'Exponentiation')} then turns the adjusted gaps into positive ratios, while {move('summation', 'summing')} and dividing make one probability distribution.",
],
44: [
    f"{move('proportionality', 'Proportionality')} states the growth pattern without pretending every implementation has the same fixed cost.",
    f"{move('powers', 'The square')} appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.",
],
45: [
    f"{move('arrows', 'Arrows')} show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.",
    f"The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.",
],
46: [
    f"{move('logarithm', 'The log')} converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.",
    f"{move('summation', 'Summing')} collects surprise from every actual next token, and {move('division', 'dividing by n')} makes sentences of different lengths comparable per token.",
    f"{move('negative-sign', 'The minus sign')} makes low probabilities costly; {move('exponential', 'the final exponential')} reverses the log scale so the answer reads like an equivalent number of equally likely choices.",
],
49: [
    f"{move('subtraction', 'Confidence minus accuracy')} finds each bin's reliability gap; adding them would measure overall level rather than disagreement.",
    f"{move('absolute-value', 'Absolute value')} makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.",
    f"{move('multiplication', 'Multiplying by |Bᵦ|/n')} gives a large bin proportionally more influence, and {move('summation', 'the sum')} combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.",
],
51: [
    f"{move('powers', 'The negative power')} makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.",
    f"{move('multiplication', 'A scales that falling term')} to the observed problem; adding A would create a floor instead of changing improvement size.",
    f"{move('addition', 'Adding B')} represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.",
],
53: [
    f"{move('subtraction', 'rA−rB')} discards any common reward offset and keeps only which answer reviewers prefer and by how much.",
    f"{move('negative-sign', 'The inner negative')} makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.",
    f"{move('exponential', 'Exponentiation')} turns an unbounded reward gap into positive odds; adding one and {move('division', 'taking the reciprocal')} squeeze the result between zero and one without changing order.",
],
77: [
    f"{move('multiplication', 'Each multiplication')} asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.",
    f"{move('summation', 'The sum')} combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.",
    f"{move('indices', 'i+j')} slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.",
],
84: [
    f"{move('multiplication', 'The two multiplications')} scale how much clean image and fresh noise survive at time t.",
    f"{move('addition', 'Addition')} overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.",
    f"{move('square-root', 'Square roots of the variance shares')} convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.",
],
85: [
    f"{move('subtraction', 'Subtracting predicted noise from actual noise')} isolates the denoiser's error rather than their combined amount.",
    f"{move('norm', 'The squared norm')} lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.",
    f"{move('expectation', 'Expectation')} averages that error over images, noise samples, and times according to how training encounters them.",
],
89: [
    f"{move('addition', 'Addition')} combines reward received now with estimated value still available afterward because both contribute to total future return.",
    f"{move('multiplication', 'γ scales future value')} to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.",
    f"{move('maximum', 'Max')} uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.",
],
90: [
    f"{move('logarithm', 'The policy log')} turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.",
    f"{move('multiplication', 'Multiplying by return G')} makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.",
    f"{move('expectation', 'Expectation')} averages this noisy sampled advice across trajectories according to how often the policy produces them.",
],
92: [
    f"{move('dot-product', 'Each dot product')} measures aligned agreement between one image representation and one candidate text representation.",
    f"{move('division', 'Dividing by temperature')} controls how strongly score gaps matter before {move('exponential', 'exponentiation')} converts them into positive relative weights.",
    f"{move('summation', 'The denominator sum')} makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.",
    f"{move('logarithm', 'Negative log')} turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.",
],
94: [
    f"{move('multiplication', 'BA')} composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.",
    f"{move('addition', 'Adding that correction to W')} preserves the pretrained base and treats adaptation as a change. {move('symbol-decorations', 'The prime on W')} marks the adapted version; replacing W would discard the knowledge we intended to keep.",
],
95: [
    f"{move('division', 'Dividing by scale s')} expresses a real weight in units of one quantization step.",
    f"{move('rounding', 'Rounding')} chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.",
    f"{move('multiplication', 'Multiplying q by s')} converts the stored step count back to the weight's approximate real scale. {move('symbol-decorations', 'The hat on w')} marks this reconstructed approximation; addition would shift levels rather than restore their unit size.",
],
102: [
    f"{move('multiplication', 'Likelihood times prior')} requires a story to have both earlier plausibility and support from the new footprint. Addition would let overwhelming prior belief compensate linearly for evidence impossible under that story.",
    f"{move('summation', 'The denominator sums support')} over every competing story to find the whole amount of belief available.",
    f"{move('division', 'Division by that total')} turns each story's support into a share summing to one, while {move('conditional-bar', 'the conditional bars')} keep “evidence given story” distinct from “story after evidence.”",
],
115: [
    f"{move('symbol-decorations', 'The bar over R')} marks the mean return, keeping what a branch has already demonstrated; see {move('mean', 'mean')}.",
    f"{move('logarithm', 'log N')} lets exploration pressure grow slowly as the parent receives more visits instead of growing in direct proportion forever.",
    f"{move('division', 'Dividing by nₐ')} makes an often-tested action less uncertain; {move('square-root', 'the square root')} tempers how sharply that exploration bonus changes.",
    f"{move('multiplication', 'c scales curiosity')} and {move('addition', 'addition')} places that exploration bonus beside observed reward. Multiplying reward and curiosity would make either zero erase the other.",
],
119: [
    f"{move('function-application', 'M(hᵥ,hᵤ)')} creates a message that depends on both receiving and neighboring nodes.",
    f"{move('summation', 'Summing over neighbors')} combines a variable-size, unordered neighborhood into one fixed-size message. Concatenation would depend on neighbor count and arbitrary listing order.",
    f"{move('function-application', 'U')} then updates the old node state using both its own previous information and the neighborhood evidence.",
],
122: [
    f"{move('probability', 'The two probabilities')} ask how likely the same released event S is with or without one person's record.",
    f"{move('membership', 'M(D) ∈ S')} says the randomized mechanism's output landed in the set of outcomes being inspected.",
    f"{move('exponential', 'e^ε')} turns the privacy budget into a multiplicative allowance: ε=0 requires equal probabilities, while larger ε permits a bounded ratio.",
    f"{move('inequalities', 'The ≤ sign')} promises a ceiling rather than false equality; privacy needs the two distributions close, not identical for every dataset pair.",
],
}

START = "### Why these operations are forced"
END_MARKER = "Only now can we compress"


def section(lines):
    body = "\n".join(f"- {line}" for line in lines)
    return f"{START}\n\n{body}\n\n"


def update(path, lines):
    text = path.read_text()
    text = re.sub(
        rf"\n{re.escape(START)}\n.*?(?=\n(?:Only now (?:can we compress|is the compact notation useful)|\#\# ))",
        "",
        text,
        flags=re.S,
    )
    marker = re.search(
        r"^Only now (?:can we compress|is the compact notation useful)[^\n]*:\s*$",
        text,
        re.M,
    )
    if not marker:
        raise ValueError(f"{path}: cannot find equation compression marker")
    text = text[:marker.start()] + section(lines) + text[marker.start():]
    path.write_text(text.rstrip() + "\n")


def main():
    equation_chapters = []
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        text = path.read_text()
        if "$$" not in text:
            continue
        number = int(path.parent.name[:3])
        equation_chapters.append(number)
        if number not in REASONS:
            raise ValueError(f"{path}: equation chapter has no operation reasoning")
        update(path, REASONS[number])
    extras = sorted(set(REASONS) - set(equation_chapters))
    if extras:
        raise ValueError(f"operation reasoning exists for non-equation chapters: {extras}")
    print(f"Added contextual operation reasoning to {len(equation_chapters)} equation-bearing excavations.")


if __name__ == "__main__":
    main()
