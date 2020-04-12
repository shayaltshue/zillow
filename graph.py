from matplotlib import pyplot as plt
import seaborn as sns

def plot_county_taxes(tax_los_angeles, tax_orange, tax_ventura):
    f, axes = plt.subplots(1, 3, figsize=(10, 6), sharex=True)
    sns.despine(left=True)

    ax1 = sns.distplot(tax_los_angeles.tax_rate, kde=True, color="hotpink", ax=axes[0])
    ax2 = sns.distplot(tax_orange.tax_rate, kde=True, color="orange", ax=axes[1])
    ax3 = sns.distplot(tax_ventura.tax_rate, kde=True, color="green", ax=axes[2])

    ax1.title.set_text('LA County')
    ax2.title.set_text('Orange County')
    ax3.title.set_text('Ventura County')
    ax1.set_ylabel('Number of Homes')
    ax2.set_ylabel('Number of Homes')
    ax3.set_ylabel('Number of Homes')
    plt.xlim(0, 0.2)

plt.subplots_adjust(bottom=10, top = 12)

def plot_features(train):
    y = train.property_value

    plt.figure(figsize=(14,6))

    # Left graph
    plt.subplot(131)
    sns.scatterplot(train.total_sqft, y)
    plt.title('Total Square Feet')
    plt.xlabel('Total Square Feet')
    plt.ylabel('Property Value')

    # Center graph
    plt.subplot(132)
    sns.scatterplot(train.bedroom_count, y)
    plt.title('Number of Bedrooms')
    plt.xlabel('# of Bedrooms')
    plt.ylabel('Property Value')

    # Right graph
    plt.subplot(133)
    sns.scatterplot(train.bathroom_count, y)
    plt.title('Number of Bathrooms')
    plt.xlabel('# of Bathrooms')
    plt.ylabel('Property Value')

    plt.suptitle('What Affects Taxes Most')
    
    
def graph_pairplot(train):
    # Figure: Pairplot of Features

    sns.pairplot(train[['total_sqft', 'bedroom_count', 'bathroom_count', 'property_value']], kind='reg')
    plt.suptitle('Correlation Between Square Feet, Bedrooms and Bathrooms', size=14, y=1.02)
    plt.figure(figsize=(16, 16))
    
def graph_corr(train):
    corr = train.corr()
    sns.heatmap(corr, cmap="BuGn")
    
def graph_train_models(predictions):
    plt.figure(figsize=(16,6))
    plt.suptitle('Model Comparison')
    plt.tight_layout()

    y = predictions.actual

    plt.subplot(221)
    plt.scatter(y=predictions.lm_sqft - y, x=y, label='Total Square Feet')
    #plt.scatter(y=predictions.baseline, x=y,  label='Baseline', color='red')
    plt.legend()

    plt.subplot(222)
    plt.scatter(y=predictions.lm_bedroom - y, x=y, label='# of Bedrooms')
    #plt.scatter(y=predictions.baseline, x=y,  label='Baseline', color='red')
    plt.legend()


    plt.subplot(223)
    plt.scatter(y=predictions.lm_bathroom -y, x=y, label='# of Bathrooms')
    #plt.scatter(y=predictions.baseline, x=y,  label='Baseline', color='red')

    plt.subplot(224)
    plt.scatter(y=predictions.lm_sqft_bed_bath - y, x=y, label='SqFt Bed and Bath')
    #plt.scatter(y=predictions.baseline, x=y,  label='Baseline', color='red')