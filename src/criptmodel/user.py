from criptmodel.utils.serializable import Serializable


class User(Serializable):
    """Base class for representing a user.

    Parameters
    ----------

    username: str, required
        The username of the user.

    full_name: str, required
        The actual full name of the user.

    email: str, required
        The email id of the user.

    phone: str, optional
        The telephone number of the user.

    website: str, optional
        The personal website of the user.

    twitter: str, optional
        The Twitter handle of the user.

    orcid: str, optional
        The ORCID (https://orcid.org/) iD of the user.

    organization: str, optional
        The organization the user belongs to.

    position: str, optional
        The position/title of the user in their organization.
    """

    def __init__(
        self,
        username: str = None,
        full_name: str = None,
        email: str = None,
        phone: str = None,
        website: str = None,
        twitter: str = None,
        orcid: str = None,
        organization: str = None,
        position: str = None,
    ):
        self._username = None
        self.username = username

        self._full_name = None
        self.full_name = full_name

        self._email = None
        self.email = email

        self._phone = None
        self.phone = phone

        self._website = None
        self.website = website

        self._twitter = None
        self.twitter = twitter

        self._orcid = None
        self.orcid = orcid

        self._organization = None
        self.organization = organization

        self._position = None
        self.position = position

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, website):
        self._website = website

    @property
    def twitter(self):
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        self._twitter = twitter

    @property
    def orcid(self):
        return self._orcid

    @orcid.setter
    def orcid(self, orcid):
        self._orcid = orcid

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, organization):
        self._organization = organization

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
